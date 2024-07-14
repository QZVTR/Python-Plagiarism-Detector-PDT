from matplotlib import pyplot as plt
from ProgramDependency import ProgramDepTree
from subOriginal import SignificantSubTreesComp
from Ngram import NgramComp
from CosineSimilarity import CosineSim
import os
import re
from tabulate import tabulate

# TODO
# 1. CREATE NEW DATASET FOR TESTING THIS WITH MUCH LARGER DIFFERENCES


def getScores():

    methods = [
        "ProgramDepTree",
        "ProgramDepTreeOld",
        "SignificantSubTreesComp",
        "NgramComp",
        "CosineSim",
    ]
    overall = {}
    for method in methods:
        if method == "ProgramDepTree":

            scores = {}
            # diff = ["Comment", "Reorder", "Variable Name"]
            diff = ["Variable Name"]

            sets = {
                "Banking System": 5,
                "Employee Management System": 5,
                "Factorial": 5,
                "File Manager": 5,
                "Long Program": 5,
                "Math Operations": 5,
                "Project Management": 5,
                "Simple Chatbot": 5,
                "Student Record System": 4,  # 5
                "Text Analyser": 5,
            }

            for prog, val in sets.items():
                for name in diff:
                    temp = []
                    folderPath = f"TpFp Datasets/{prog}/{name}"
                    folderFiles = [
                        file
                        for file in os.listdir(folderPath)
                        if not file.startswith(".DS_Store") and file.endswith(".py")
                    ]

                    for file in folderFiles:
                        plag = False
                        versionNumber = int(re.search(r"v(\d+)\.py", file).group(1))
                        idx = f"{prog} {name}"
                        filePath1 = f"TpFp Datasets/{prog}/{name}/program_v1.py"
                        filePath2 = os.path.join(folderPath, file)

                        if versionNumber < val:
                            plag = True

                        # print(versionNumber)
                        comp = ProgramDepTree()
                        pdg1 = comp.generatePdtFromFile(filePath1)
                        pdg2 = comp.generatePdtFromFile(filePath2)
                        res = comp.calculateSimilarity(pdg1, pdg2)
                        # print(res)
                        temp.append([plag, round(res, 4)])
                    scores[idx] = temp
            overall[method] = scores
        elif method == "ProgramDepTreeOld":
            scores = {}
            diff = ["Variable Name"]

            sets = {
                "Banking System": 5,
                "Employee Management System": 5,
                "Factorial": 5,
                "File Manager": 5,
                "Long Program": 5,
                "Math Operations": 5,
                "Project Management": 5,
                "Simple Chatbot": 5,
                "Student Record System": 4,  # 5
                "Text Analyser": 5,
            }
            for prog, val in sets.items():
                for name in diff:
                    temp = []
                    folderPath = f"TpFp Datasets/{prog}/{name}"
                    folderFiles = [
                        file
                        for file in os.listdir(folderPath)
                        if not file.startswith(".DS_Store") and file.endswith(".py")
                    ]

                    for file in folderFiles:
                        plag = False
                        versionNumber = int(re.search(r"v(\d+)\.py", file).group(1))
                        idx = f"{prog} {name}"
                        filePath1 = f"TpFp Datasets/{prog}/{name}/program_v1.py"
                        filePath2 = os.path.join(folderPath, file)

                        if versionNumber < val:
                            plag = True

                        comp = ProgramDepTree()
                        pdg1 = comp.generatePdtFromFile(filePath1, v="old")
                        pdg2 = comp.generatePdtFromFile(filePath2, v="old")
                        res = comp.calculateSimilarity(pdg1, pdg2)
                        # print(res)
                        temp.append([plag, round(res, 4)])
                    scores[idx] = temp
            overall[method] = scores
        elif method == "SignificantSubTreesComp":
            scores = {}
            diff = ["Variable Name"]

            sets = {
                "Banking System": 5,
                "Employee Management System": 5,
                "Factorial": 5,
                "File Manager": 5,
                "Long Program": 5,
                "Math Operations": 5,
                "Project Management": 5,
                "Simple Chatbot": 5,
                "Student Record System": 4,  # 5
                "Text Analyser": 5,
            }
            for prog, val in sets.items():
                for name in diff:
                    temp = []
                    folderPath = f"TpFp Datasets/{prog}/{name}"
                    folderFiles = [
                        file
                        for file in os.listdir(folderPath)
                        if not file.startswith(".DS_Store") and file.endswith(".py")
                    ]
                    for file in folderFiles:
                        idx = f"{prog} {name}"
                        plag = False
                        versionNumber = int(re.search(r"v(\d+)\.py", file).group(1))
                        filePath1 = f"TpFp Datasets/{prog}/{name}/program_v1.py"
                        filePath2 = os.path.join(folderPath, file)

                        if versionNumber < val:
                            plag = True

                        comp = SignificantSubTreesComp(filePath1, filePath2)
                        res = comp.compareSubTrees(reorderDepth=10000)
                        temp.append([plag, res[0]])
                    scores[idx] = temp
            overall[method] = scores
        elif method == "NgramComp":
            scores = {}
            diff = ["Variable Name"]

            sets = {
                "Banking System": 5,
                "Employee Management System": 5,
                "Factorial": 5,
                "File Manager": 5,
                "Long Program": 5,
                "Math Operations": 5,
                "Project Management": 5,
                "Simple Chatbot": 5,
                "Student Record System": 4,  # 5
                "Text Analyser": 5,
            }
            for prog, val in sets.items():
                for name in diff:
                    temp = []
                    folderPath = f"TpFp Datasets/{prog}/{name}"
                    folderFiles = [
                        file
                        for file in os.listdir(folderPath)
                        if not file.startswith(".DS_Store") and file.endswith(".py")
                    ]
                    for file in folderFiles:
                        idx = f"{prog} {name}"
                        plag = False
                        versionNumber = int(re.search(r"v(\d+)\.py", file).group(1))
                        filePath1 = f"TpFp Datasets/{prog}/{name}/program_v1.py"
                        filePath2 = os.path.join(folderPath, file)

                        if versionNumber < val:
                            plag = True

                        comp = NgramComp()
                        res = comp.jaccardSimilarity(filePath1, filePath2, 3)
                        temp.append([plag, round(res, 3)])
                    scores[idx] = temp
            overall[method] = scores

        elif method == "CosineSim":
            scores = {}
            diff = ["Variable Name"]

            sets = {
                "Banking System": 5,
                "Employee Management System": 5,
                "Factorial": 5,
                "File Manager": 5,
                "Long Program": 5,
                "Math Operations": 5,
                "Project Management": 5,
                "Simple Chatbot": 5,
                "Student Record System": 4,
                "Text Analyser": 5,
            }
            for prog, val in sets.items():
                for name in diff:
                    temp = []
                    folderPath = f"TpFp Datasets/{prog}/{name}"
                    folderFiles = [
                        file
                        for file in os.listdir(folderPath)
                        if not file.startswith(".DS_Store") and file.endswith(".py")
                    ]
                    for file in folderFiles:
                        idx = f"{prog} {name}"
                        plag = False
                        versionNumber = int(re.search(r"v(\d+)\.py", file).group(1))
                        filePath1 = f"TpFp Datasets/{prog}/{name}/program_v1.py"
                        filePath2 = os.path.join(folderPath, file)

                        if versionNumber < val:
                            plag = True

                        comp = CosineSim()
                        res = comp.computeCosineSimilarity(filePath1, filePath2)
                        temp.append([plag, round(res, 3)])
                    scores[idx] = temp
            overall[method] = scores
    return overall


def parseMatches(matches, t):
    scores = [vals for key, vals in matches.items()]
    Tp, Fp, Tn, Fn = 0, 0, 0, 0
    for programScores in scores:
        for match in programScores:
            plagiarised, score = match
            # print(score)
            if plagiarised:
                if score >= t:
                    Tp += 1
                else:
                    Fn += 1
            else:
                if score >= t:
                    Fp += 1
                else:
                    Tn += 1
    return Tp, Fp, Tn, Fn


def graph(rocData, thresholds):
    print(rocData)
    plt.figure()
    plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
    # plt.plot([0, 0, 0, 0], [29, 31, 0, 0])

    for (Tp, Fp, Tn, Fn), threshold in zip(rocData, thresholds):
        if Fp == 0:
            fpr = 0
        else:
            fpr = Fp / (Fp + Tn)

        tpr = Tp / (Tp + Fn)

        plt.plot(fpr, tpr, lw=2, label=f"Threshold: {threshold}")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.legend(loc="lower right")
    plt.show()


def calculateRecall(Tp, Fn):
    if Tp + Fn == 0:
        return 0
    else:
        return Tp / (Tp + Fn)


def calculatePrecision(Tp, Fp):
    if Tp + Fp == 0:
        return 0
    else:
        return Tp / (Tp + Fp)


def calculateF1Score(precision, recall):
    if precision + recall == 0:
        return 0
    else:
        return 2 * ((precision * recall) / (precision + recall))


def calculateAccuracy(Tp, Fp, Tn, Fn):
    totalInstances = Tp + Fp + Tn + Fn
    if totalInstances == 0:
        return 0
    else:
        correctPredictions = Tp + Tn
        return correctPredictions / totalInstances


def initialiseScores():
    data = getScores()
    return data


def getMetrics(data):
    thresholds = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.9, 0.95]
    # print(data)
    tableData = []
    headers = [
        "Method",
        "Threshold",
        "Tp",
        "Fp",
        "Tn",
        "Fn",
        "Precision↑",
        "Recall↑",
        "F1 Score↑",
        "Accuracy↑",
    ]

    for method, scores in data.items():
        for t in thresholds:
            row = [method, t]
            # print(f"Method: {method}, Threshold: {t}")
            Tp, Fp, Tn, Fn = parseMatches(scores, t)
            # print(f"Tp: {Tp}, Fp: {Fp}, Tn: {Tn}, Fn: {Fn}")
            precision = calculatePrecision(Tp, Fp)
            recall = calculateRecall(Tp, Fn)
            f1Score = calculateF1Score(precision, recall)
            accuracy = calculateAccuracy(Tp, Fp, Tn, Fn)

            row.extend(
                [
                    Tp,
                    Fp,
                    Tn,
                    Fn,
                    round(precision, 3),
                    round(recall, 3),
                    round(f1Score, 3),
                    round(accuracy, 3),
                ]
            )
            tableData.append(row)

            # print("Precision:", round(precision, 3))
            # print("Recall:", round(recall, 3))
            # print("F1 Score:", round(f1Score, 3))
            # print("Accuracy:", round(accuracy, 3))
            # print()
    print(tabulate(tableData, headers=headers))


def getMetricsWithAverage(data):
    thresholds = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.9, 0.95]
    tableData = []
    headers = [
        "Method",
        "Threshold",
        "Precision↑",
        "Recall↑",
        "F1 Score↑",
        "Accuracy↑",
    ]

    for method, scores in data.items():
        methodMetrics = []
        for t in thresholds:

            Tp, Fp, Tn, Fn = parseMatches(scores, t)
            precision = calculatePrecision(Tp, Fp)
            recall = calculateRecall(Tp, Fn)
            f1Score = calculateF1Score(precision, recall)
            accuracy = calculateAccuracy(Tp, Fp, Tn, Fn)

            methodMetrics.append([precision, recall, f1Score, accuracy])

        # Calculate average metrics for the method across all thresholds
        avgPrecison = sum(metric[0] for metric in methodMetrics) / len(methodMetrics)
        avgRecall = sum(metric[1] for metric in methodMetrics) / len(methodMetrics)
        avgF1Score = sum(metric[2] for metric in methodMetrics) / len(methodMetrics)
        avgAccuracy = sum(metric[3] for metric in methodMetrics) / len(methodMetrics)

        row = [method, "Average"]
        row.extend(
            [
                round(avgPrecison, 3),
                round(avgRecall, 3),
                round(avgF1Score, 3),
                round(avgAccuracy, 3),
            ]
        )
        tableData.append(row)

    print(tabulate(tableData, headers=headers))


def displayGraph(data, m):
    thresholds = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.9, 0.95]
    rocData = []
    for method, scores in data.items():
        if method == m:
            for t in thresholds:
                print(f"Method: {method}, Threshold: {t}")
                Tp, Fp, Tn, Fn = parseMatches(scores, t)
                print(f"Tp: {Tp}, Fp: {Fp}, Tn: {Tn}, Fn: {Fn}")
                rocData.append((Tp, Fp, Tn, Fn))

    graph(rocData, thresholds)


methods = [
    "ProgramDepTree",
    "ProgramDepTreeOld",
    "SignificantSubTreesComp",
    "NgramComp",
    "CosineSim",
]

data = initialiseScores()
# getMetrics(data)
getMetricsWithAverage(data)
# displayGraph(data, methods[0])
