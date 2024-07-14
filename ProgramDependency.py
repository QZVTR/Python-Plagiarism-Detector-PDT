import ast
import networkx as nx
import re


class ProgramDepTree:
    def __init__(self):
        pass

    def generatePdtFromFile(self, filePath, v="current"):
        """
        Generate Program Dependency Graph (pdt) from Python code in a file.
        """

        if v == "current":
            with open(filePath, "r") as file:
                code = file.read()
            return self._generatePdt(code)
        elif v == "old":
            with open(filePath, "r") as file:
                code = file.read()
            return self._generatePdtOld(code)

    def _generatePdt(self, code):
        """
        Generate Program Dependency Graph (pdt) from Python code.
        """
        # Initialise graph
        graph = nx.DiGraph(arrows=True)
        # Parse tree
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        graph.add_node(target.id, type="variable")
                    elif isinstance(target, ast.Subscript):
                        if isinstance(target.value, ast.Name):
                            graph.add_node(target.value.id, type="variable")

                if isinstance(node.value, ast.Name):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            graph.add_edge(node.value.id, target.id)
                elif isinstance(node.value, ast.Attribute):
                    if isinstance(node.value.value, ast.Name):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                graph.add_edge(node.value.value.id, target.id)
                elif isinstance(node.value, ast.Call):
                    if isinstance(node.value.func, ast.Name):
                        funcName = node.value.func.id
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                graph.add_node(funcName, type="function")
                                graph.add_edge(funcName, target.id)
                    elif isinstance(node.value.func, ast.Attribute):
                        funcName = node.value.func.attr
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                graph.add_node(funcName, type="function")
                                graph.add_edge(funcName, target.id)
            elif isinstance(node, ast.FunctionDef):
                graph.add_node(
                    node.name,
                    type="function",
                    IfStatements=0,
                    IfOperations=[],
                    IfReturns=[],
                    ForLoops=0,
                    ForLoopOps=[],
                    WhileLoops=0,
                    WhileLoopOps=[],
                )
                for arg in node.args.args:
                    if arg.arg != "self":
                        arg_id = f"{arg.arg}_{id(node)}"
                        graph.add_node(arg_id, type="variable")
                        graph.add_edge(node.name, arg_id)
                for stmt in node.body:
                    # print(stmt)
                    if isinstance(stmt, ast.Return):
                        self._handleReturnStatement(graph, node.name, stmt.value)

                    elif isinstance(stmt, ast.Assign):
                        self._handleFunctionOperations(graph, node.name, stmt.value)

                    elif isinstance(stmt, ast.If):
                        self._handleIfObject(graph, node.name, stmt)

                    elif isinstance(stmt, ast.For):
                        self._handleForLoop(graph, node.name, stmt)

                    elif isinstance(stmt, ast.While):
                        self._handleWhileLoop(graph, node.name, stmt)

                    ast.NodeVisitor().visit(stmt)

            elif isinstance(node, ast.Import):
                for alias in node.names:
                    graph.add_node(alias.name, type="import")

            elif isinstance(node, ast.ClassDef):
                # Handle class definitions
                graph.add_node(node.name, type="class")

                for bodyItem in node.body:
                    if isinstance(bodyItem, ast.FunctionDef):
                        graph.add_node(
                            bodyItem.name,
                            type="function",
                            within_class=node.name,
                            operations=[],
                            IfStatements=0,
                            IfOperations=[],
                            IfReturns=[],
                            ForLoops=0,
                            ForLoopOps=[],
                            WhileLoops=0,
                            WhileLoopOps=[],
                        )
                        graph.add_edge(node.name, bodyItem.name, relation="has_method")

                        for arg in bodyItem.args.args:
                            if arg.arg != "self":  # Ignoring 'self'
                                arg_id = f"{arg.arg}_{id(bodyItem)}"
                                graph.add_node(
                                    arg_id,
                                    type="variable",
                                    within_function=bodyItem.name,
                                )
                                graph.add_edge(
                                    bodyItem.name, arg_id, relation="has_argument"
                                )

                        for stmt in bodyItem.body:

                            if isinstance(stmt, ast.Return):
                                self._handleReturnStatement(
                                    graph, bodyItem.name, stmt.value
                                )
                            # elif isinstance(stmt, ast.Assign):  # changes here
                            #    self.handleFunctionOperations(
                            #        graph, bodyItem.name, stmt.value
                            #    )
                            ast.NodeVisitor().visit(stmt)

                    elif isinstance(bodyItem, ast.Assign):
                        # Assuming simple assignments for class variables
                        for target in bodyItem.targets:
                            if isinstance(target, ast.Name):
                                graph.add_node(
                                    target.id,
                                    type="class_variable",
                                    within_class=node.name,
                                )
                                graph.add_edge(
                                    node.name, target.id, relation="has_variable"
                                )
        # self._printGraph(graph)
        return graph

    def _generatePdtOld(self, code):
        """
        Generate Program Dependency Graph (pdt) from Python code. (Old Version)
        """
        # remCode = self.removeComments(code)

        graph = nx.DiGraph(arrows=True)
        tree = ast.parse(code)

        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        graph.add_node(target.id, type="variable")
                    elif isinstance(target, ast.Subscript):
                        if isinstance(target.value, ast.Name):
                            graph.add_node(target.value.id, type="variable")

                if isinstance(node.value, ast.Name):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            graph.add_edge(node.value.id, target.id)
                elif isinstance(node.value, ast.Attribute):
                    if isinstance(node.value.value, ast.Name):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                graph.add_edge(node.value.value.id, target.id)
                elif isinstance(node.value, ast.Call):
                    if isinstance(node.value.func, ast.Name):
                        funcName = node.value.func.id
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                graph.add_node(funcName, type="function")
                                graph.add_edge(funcName, target.id)
                    elif isinstance(node.value.func, ast.Attribute):
                        funcName = node.value.func.attr
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                graph.add_node(funcName, type="function")
                                graph.add_edge(funcName, target.id)
            elif isinstance(node, ast.FunctionDef):
                graph.add_node(node.name, type="function")
                for arg in node.args.args:
                    if arg.arg != "self":
                        graph.add_node(arg.arg, type="variable")
                        graph.add_edge(node.name, arg.arg)
                for stmt in node.body:
                    if isinstance(stmt, ast.Return):
                        if isinstance(stmt.value, ast.Name):
                            graph.add_edge(node.name, stmt.value.id)
                    ast.NodeVisitor().visit(stmt)

            elif isinstance(node, ast.Import):
                for alias in node.names:
                    graph.add_node(alias.name, type="import")

            elif isinstance(node, ast.ClassDef):
                # Handle class definitions
                graph.add_node(node.name, type="class")

                for bodyItem in node.body:
                    if isinstance(bodyItem, ast.FunctionDef):
                        graph.add_node(
                            bodyItem.name, type="function", within_class=node.name
                        )
                        graph.add_edge(node.name, bodyItem.name, relation="has_method")

                        for arg in bodyItem.args.args:
                            if arg.arg != "self":  # Ignoring 'self'
                                graph.add_node(
                                    arg.arg,
                                    type="variable",
                                    within_function=bodyItem.name,
                                )
                                graph.add_edge(
                                    bodyItem.name, arg.arg, relation="has_argument"
                                )

                        for stmt in bodyItem.body:
                            if isinstance(stmt, ast.Return):
                                if isinstance(stmt.value, ast.Name):
                                    graph.add_edge(
                                        bodyItem.name,
                                        stmt.value.id,
                                        relation="returns",
                                    )
                            ast.NodeVisitor().visit(stmt)

                    elif isinstance(bodyItem, ast.Assign):
                        # Assuming simple assignments for class variables
                        for target in bodyItem.targets:
                            if isinstance(target, ast.Name):
                                graph.add_node(
                                    target.id,
                                    type="class_variable",
                                    within_class=node.name,
                                )
                                graph.add_edge(
                                    node.name, target.id, relation="has_variable"
                                )

        # self._printTree(tree)
        # self._printGraph(graph)

        return graph

    def _extractOperations(self, body, operations):
        for stmt in body:
            if isinstance(stmt, ast.BinOp):
                op_type = type(stmt.op).__name__
                operations.append(op_type)
            elif isinstance(stmt, ast.Compare):
                op_types = [type(op).__name__ for op in stmt.ops]
                operations.extend(op_types)
            elif isinstance(stmt, ast.Return):
                if isinstance(stmt.value, ast.BinOp):
                    op_type = type(stmt.value.op).__name__
                    operations.append(op_type)
                # Handle other types of return values if needed
            elif isinstance(stmt, ast.If):
                self._extractOperations(stmt.body, operations)

    def _handleForLoop(self, graph, functionName, ForLoopNode):
        operations = []
        for bodyNode in ForLoopNode.body:
            # print(bodyNode)
            if isinstance(bodyNode, ast.AugAssign):
                operations.append(type(bodyNode.op).__name__)
            elif isinstance(bodyNode, ast.Expr):
                if isinstance(bodyNode.value, ast.Compare):
                    op = bodyNode.value.ops[0]  # Assuming one comparison
                    operations.append(type(op).__name__)
        graph.nodes[functionName]["ForLoops"] += 1
        graph.nodes[functionName]["ForLoopOps"] += operations

    def _handleWhileLoop(self, graph, functionName, WhileLoopNode):
        operations = []
        for bodyNode in WhileLoopNode.body:
            # print(bodyNode)
            if isinstance(bodyNode, ast.AugAssign):
                operations.append(type(bodyNode.op).__name__)
            elif isinstance(bodyNode, ast.Expr):
                if isinstance(bodyNode.value, ast.Compare):
                    op = bodyNode.value.ops[0]  # Assuming one comparison
                    operations.append(type(op).__name__)
        graph.nodes[functionName]["WhileLoops"] += 1
        graph.nodes[functionName]["WhileLoopOps"] += operations

    def _handleIfObject(self, graph, functionName, IfNode):
        """
        Handle returns and operations of if statements (only works on extremely basic if statements)
        """
        operations = []

        # Extract operations from the if statement's body
        self._extractOperations(IfNode.body, operations)

        graph.nodes[functionName]["IfReturns"] += operations

        # print(f"{functionName}: {IfNode.test}")
        graph.nodes[functionName]["IfStatements"] += 1
        if IfNode.test:
            res = self._handleIfOperations(graph, functionName, IfNode.test)

        # if IfNode.body:
        #    res = self._handleIfStatementReturns(graph, functionName, IfNode.body)

        # for stmt in IfNode.body:
        #    print(f"{functionName}: {stmt}")

    def _handleIfOperations(self, graph, functionName, value):
        """
        Handle binary and comparison operations within a function.
        """
        # print(f"{value}")
        if isinstance(value, ast.BinOp):
            opMap = {
                ast.Add: "Add",
                ast.Sub: "Sub",
                ast.Mult: "Mult",
                ast.Div: "Div",
                ast.FloorDiv: "FloorDiv",
                ast.Mod: "Mod",
                ast.Pow: "Pow",
                ast.LShift: "LShift",
                ast.RShift: "RShift",
                ast.BitOr: "BitOr",
                ast.BitXor: "BitXor",
                ast.BitAnd: "BitAnd",
                ast.MatMult: "MatMult",
            }
            opType = opMap.get(type(value.op), "Unknown")
            opId = f"BinOp_{id(value)}"
            graph.add_node(opId, type="binary_op")
            graph.add_edge(functionName, opId, relation="if_operation")
            # operations = graph.nodes[functionName].get("operations", [])
            graph.nodes[functionName]["IfOperations"] += [opType]

        elif isinstance(value, ast.Compare):
            op = value.ops[0]  # Assuming only one comparison operator
            opType = type(op).__name__
            opId = f"CompOp_{id(value)}"
            # graph.add_node(opId, type="comparison_op")
            # graph.add_edge(functionName, opId, relation="if_operation")

            # Add the comparison operation and comparators to the graph node
            if "IfOperations" not in graph.nodes[functionName]:
                graph.nodes[functionName]["IfOperations"] = [opType]
            else:
                graph.nodes[functionName]["IfOperations"].append(opType)

    def _handleIfStatementReturns(self, graph, functionName, returnValue):
        """
        Handle return statement nodes and edges.
        """
        # print(returnValue)

        if isinstance(returnValue, ast.Name):
            graph.add_edge(functionName, returnValue.id, relation="returns")
            graph.nodes[functionName]["IfReturns"] += [returnValue.id]
            # graph.nodes[functionName]["binaryOp"] = "None"
        elif isinstance(returnValue, ast.BinOp):
            opMap = {
                ast.Add: "Add",
                ast.Sub: "Sub",
                ast.Mult: "Mult",
                ast.Div: "Div",
                ast.FloorDiv: "FloorDiv",
                ast.Mod: "Mod",
                ast.Pow: "Pow",
                ast.LShift: "LShift",
                ast.RShift: "RShift",
                ast.BitOr: "BitOr",
                ast.BitXor: "BitXor",
                ast.BitAnd: "BitAnd",
                ast.MatMult: "MatMult",
            }
            opType = opMap.get(type(returnValue.op), "Unknown")
            opId = f"BinOp_{id(returnValue)}"
            graph.add_node(opId, type="binary_op")
            graph.add_edge(functionName, opId, relation="if_returns")
            returns = []
            if isinstance(returnValue.left, ast.Name):
                returns.append(returnValue.left.id)
            if isinstance(returnValue.right, ast.Name):
                returns.append(returnValue.right.id)
            graph.nodes[functionName]["IfReturns"] += [returns]
            # graph.nodes[functionName]["binaryOp"] = opType
        elif isinstance(returnValue, ast.Call):
            callId = f"Call_{id(returnValue)}"
            graph.add_node(callId, type="function_call")
            graph.add_edge(functionName, callId, relation="if_returns")
            graph.nodes[functionName]["IfReturns"] += [ast.dump(returnValue.func)]
            # graph.nodes[functionName]["binaryOp"] = "None"
        elif isinstance(returnValue, ast.Compare):
            op = returnValue.ops[0]  # Assuming only one comparison operator
            opType = type(op).__name__
            opId = f"CompOp_{id(returnValue)}"
            graph.add_node(opId, type="comparison_op")
            graph.add_edge(functionName, opId, relation="if_returns")
            # Extract the left and right comparators
            comparators = [returnValue.left.id]  # Add left comparator
            comparators.extend(
                comp.id for comp in returnValue.comparators
            )  # Add additional comparators

            # Add the comparison operation and comparators to the graph node
            graph.nodes[functionName]["IfReturns"] += opType
            # graph.nodes[functionName]["binaryOp"] = opType
        else:
            graph.nodes[functionName]["IfReturns"] = []
            # graph.nodes[functionName]["binaryOp"] = "None"

    def _handleFunctionOperations(self, graph, functionName, value):
        """
        Handle binary and comparison operations within a function.
        """
        if isinstance(value, ast.BinOp):
            opMap = {
                ast.Add: "Add",
                ast.Sub: "Sub",
                ast.Mult: "Mult",
                ast.Div: "Div",
                ast.FloorDiv: "FloorDiv",
                ast.Mod: "Mod",
                ast.Pow: "Pow",
                ast.LShift: "LShift",
                ast.RShift: "RShift",
                ast.BitOr: "BitOr",
                ast.BitXor: "BitXor",
                ast.BitAnd: "BitAnd",
                ast.MatMult: "MatMult",
            }
            opType = opMap.get(type(value.op), "Unknown")
            opId = f"BinOp_{id(value)}"
            graph.add_node(opId, type="binary_op")
            graph.add_edge(functionName, opId, relation="has_operation")
            # operations = graph.nodes[functionName].get("operations", [])
            graph.nodes[functionName]["operations"] += [opType]

        elif isinstance(value, ast.Compare):
            op = value.ops[0]  # Assuming only one comparison operator
            opType = type(op).__name__
            opId = f"CompOp_{id(value)}"
            graph.add_node(opId, type="comparison_op")
            graph.add_edge(functionName, opId, relation="has_operation")

            # Add the comparison operation and comparators to the graph node
            if "operations" not in graph.nodes[functionName]:
                graph.nodes[functionName]["operations"] = [opType]
            else:
                graph.nodes[functionName]["operations"].append(opType)

    def _handleReturnStatement(self, graph, functionName, returnValue):
        """
        Handle return statement nodes and edges.
        """
        if isinstance(returnValue, ast.Name):
            graph.add_edge(functionName, returnValue.id, relation="returns")
            graph.nodes[functionName]["returns"] = [returnValue.id]
            graph.nodes[functionName]["binaryOp"] = "None"
        elif isinstance(returnValue, ast.BinOp):
            opMap = {
                ast.Add: "Add",
                ast.Sub: "Sub",
                ast.Mult: "Mult",
                ast.Div: "Div",
                ast.FloorDiv: "FloorDiv",
                ast.Mod: "Mod",
                ast.Pow: "Pow",
                ast.LShift: "LShift",
                ast.RShift: "RShift",
                ast.BitOr: "BitOr",
                ast.BitXor: "BitXor",
                ast.BitAnd: "BitAnd",
                ast.MatMult: "MatMult",
            }
            opType = opMap.get(type(returnValue.op), "Unknown")
            opId = f"BinOp_{id(returnValue)}"
            graph.add_node(opId, type="binary_op", op=opType)
            graph.add_edge(functionName, opId, relation="returns")
            returns = []
            if isinstance(returnValue.left, ast.Name):
                returns.append(returnValue.left.id)
            if isinstance(returnValue.right, ast.Name):
                returns.append(returnValue.right.id)
            graph.nodes[functionName]["returns"] = returns
            graph.nodes[functionName]["binaryOp"] = opType
        elif isinstance(returnValue, ast.Call):
            callId = f"Call_{id(returnValue)}"
            graph.add_node(callId, type="function_call")
            graph.add_edge(functionName, callId, relation="returns")
            graph.nodes[functionName]["returns"] = [ast.dump(returnValue.func)]
            graph.nodes[functionName]["binaryOp"] = "None"
        elif isinstance(returnValue, ast.Compare):
            op = returnValue.ops[0]  # Assuming only one comparison operator
            opType = type(op).__name__
            opId = f"CompOp_{id(returnValue)}"
            graph.add_node(opId, type="comparison_op", op=opType)
            graph.add_edge(functionName, opId, relation="returns")
            # Extract the left and right comparators
            comparators = [returnValue.left.id]  # Add left comparator
            comparators.extend(
                comp.id for comp in returnValue.comparators
            )  # Add additional comparators

            # Add the comparison operation and comparators to the graph node
            graph.nodes[functionName]["returns"] = comparators
            graph.nodes[functionName]["binaryOp"] = opType
        else:
            graph.nodes[functionName]["returns"] = "Unknown"
            graph.nodes[functionName]["binaryOp"] = "None"

    def _removeSuffix(self, commonList):
        """
        Remove suffix from node id names in the list.
        """
        # print(commonList)

        for idx, node in enumerate(commonList):
            # Check if the node name contains a suffix
            if "_" in node:
                # Remove the suffix
                updatedName = re.sub(r"_\d+$", "", node)
                commonList[idx] = updatedName
        return commonList

    def calculateSimilarity(self, graph1, graph2):
        """
        Calculate Jaccard similarity coefficient between two graphs.
        """
        graph1NodesArr = list(graph1.nodes())
        graph2NodesArr = list(graph2.nodes())

        graph1NodesSuffixArr = self._removeSuffix(graph1NodesArr)
        graph2NodesSuffixArr = self._removeSuffix(graph2NodesArr)

        nodes1 = set(graph1NodesSuffixArr)
        nodes2 = set(graph2NodesSuffixArr)

        # print(f"{nodes1}\n--------------------\n{nodes2}")

        intersection = nodes1.intersection(nodes2)
        union = nodes1.union(nodes2)

        return len(intersection) / len(union) if len(union) > 0 else 0

    def _calculateStructuralSimilarity(self, graph1, graph2, node1, node2):
        """
        Calculate structural similarity based on the neighbors of the nodes.
        """
        neighbours1 = list(graph1.neighbors(node1[0]))
        neighbours2 = list(graph2.neighbors(node2[0]))

        graph1Suffix = self._removeSuffix(neighbours1)
        graph2Suffix = self._removeSuffix(neighbours2)

        nodesNeighbours1 = set(graph1Suffix)
        nodesNeighbours2 = set(graph2Suffix)

        # Simple Jaccard similarity for neighbors
        intersection = len(nodesNeighbours1.intersection(nodesNeighbours2))
        union = len(nodesNeighbours1.union(nodesNeighbours2))
        return intersection / union if union > 0 else 0

    def _printTree(self, node, level=0):
        """
        Print the abstract syntax tree in a user-friendly format.
        """
        print("  " * level + node.__class__.__name__)
        for child in ast.iter_child_nodes(node):
            self._printTree(child, level + 1)

    def _printGraph(self, graph):
        """
        Print the nodes and edges of the graph.
        """
        print("Nodes:")
        for node, data in graph.nodes(data=True):
            print(f"  {node}: {data}")
        print("Edges:")
        for edge in graph.edges():
            print(f"  {edge}")

    def findBestMatchingElements(self, graph1, graph2, t=0.5):
        """
        Find and store the best matching elements (nodes) between two graphs.
        """
        matches = []
        for node1 in graph1.nodes(data=True):
            bestMatch = None
            bestSimilarity = 0
            for node2 in graph2.nodes(data=True):
                basicSimilarity = self._calculateNodeSimilarity(node1, node2)
                structuralSimilarity = self._calculateStructuralSimilarity(
                    graph1, graph2, node1, node2
                )

                combinedSimilarity = (
                    basicSimilarity + structuralSimilarity
                ) / 2  # Average of both similarities

                if combinedSimilarity > bestSimilarity:
                    bestSimilarity = combinedSimilarity
                    bestMatch = node2
            # Change to 0.0 if only using this similarity
            if bestMatch and bestSimilarity >= t:
                matches.append((node1, bestMatch, round(bestSimilarity, 2)))

        # Sort matches by similarity score in descending order
        matches.sort(key=lambda x: x[2], reverse=True)
        return matches

    def _calculateNodeSimilarity(self, node1, node2):
        """
        Calculate similarity between two nodes based on multiple criteria, such as type,
        presence in function/class, and specific attributes.
        """
        score = 0
        maxScore = 12.5  # Adjust based on the criteria used

        # Check if both nodes are of the same type (function, variable, etc.)
        if "type" in node1[1] and "type" in node2[1]:
            if node1[1]["type"] == node2[1]["type"]:
                score += 1  # Increment score for type match

        if "op" in node1[1] and "op" in node2[1]:
            if node1[1]["op"] == node2[1]["op"]:
                score += 1
        else:
            maxScore -= 1

        # For functions and variables, check if they belong to the same class
        if "within_class" in node1[1] and "within_class" in node2[1]:
            score += 0.5
            if node1[1]["within_class"] == node2[1]["within_class"]:
                score += 1

        if "within_function" in node1[1] and "within_function" in node2[1]:
            score += 0.5
            if node1[1]["within_function"] == node2[1]["within_function"]:
                score += 1

        if "binaryOp" in node1[1] and "binaryOp" in node2[1]:
            if (
                "returns" in node1[1]
                and "returns" in node2[1]
                and len(node1[1]["returns"]) == len(node2[1]["returns"])
            ):
                score += 0.5
                if node1[1]["binaryOp"] == node2[1]["binaryOp"]:
                    score += 1
        else:
            maxScore -= 1.5

        if (
            "operations" in node1[1]
            and "operations" in node2[1]
            and len(node1[1]["operations"]) > 0
        ):
            if (
                len(node1[1]["operations"]) == len(node2[1]["operations"])
                and len(node1[1]["operations"]) > 0
                and len(node2[1]["operations"]) > 0
            ):
                score += 0.2
                score += self._operationsSim(
                    node1[1]["operations"], node2[1]["operations"]
                )
        else:
            maxScore -= 1.2

        if (
            "ForLoops" in node1[1]
            and "ForLoops" in node2[1]
            and "ForLoopsOps" in node1[1]
            and "ForLoopsOps" in node2[1]
        ):
            if (
                node1[1]["ForLoops"] == node2[1]["ForLoops"]
                and len(node1[1]["ForLoops"]) > 0
            ):
                if (
                    len(node1[1]["ForLoopsOps"]) == len(node2[1]["ForLoopsOps"])
                    and len(node1[1]["ForLoopsOps"]) > 0
                ):
                    score += 0.3
                    score += self._operationsSim(
                        node1[1]["ForLoopsOps"], node2[1]["ForLoopsOps"]
                    )
            else:
                maxScore -= 1.3
        else:
            maxScore -= 1.3

        if (
            "WhileLoops" in node1[1]
            and "WhileLoops" in node2[1]
            and "WhileLoopsOps" in node1[1]
            and "WhileLoopsOps" in node2[1]
        ):
            if (
                node1[1]["WhileLoops"] == node2[1]["WhileLoops"]
                and len(node1[1]["WhileLoops"]) > 0
            ):

                if (
                    len(node1[1]["WhileLoopsOps"]) == len(node2[1]["WhileLoopsOps"])
                    and len(node1[1]["WhileLoopsOps"]) > 0
                ):
                    score += 0.3
                    score += self._operationsSim(
                        node1[1]["WhileLoopsOps"], node2[1]["WhileLoopsOps"]
                    )
            else:
                maxScore -= 1.3
        else:
            maxScore -= 1.3

        if (
            "IfStatements" in node1[1]
            and "IfStatements" in node2[1]
            and "IfStatementsOps" in node1[1]
            and "IfStatementsOps" in node2[1]
        ):
            if (
                node1[1]["IfStatements"] == node2[1]["IfStatements"]
                and len(node1[1]["IfStatements"]) > 0
            ):

                if (
                    len(node1[1]["IfOperations"]) == len(node2[1]["IfOperations"])
                    and len(node1[1]["IfOperations"]) > 0
                ):
                    score += 0.2
                    score += self._operationsSim(
                        node1[1]["IfOperations"], node2[1]["IfOperations"]
                    )
            else:
                maxScore -= 1.2
        else:  # Added
            maxScore -= 1.2

        # Compare names for a more direct similarity
        if node1[0] == node2[0]:
            score += 0.5

        # Normalise the score based on the maximum possible score
        similarityScore = score / maxScore

        return similarityScore

    def _operationsSim(self, a, b):
        matches = sum(1 for x, y in zip(a, b) if x == y)

        # Calculate the similarity score
        score = (len(a) - matches) / len(a)
        return score
