import timeit
from ProgramDependency import ProgramDepTree
import os


def testing():

    diff = ["Comment", "Reorder", "Variable Name"]

    numRuns = 0
    totalExecutionTime = 0
    
    sets = {
        "Banking System": [5, 5, 5],
        "Employee Management System": [5, 5, 5],
        "Factorial": [5, 3, 5],
        "File Manager": [5, 5, 5],
        "Long Program": [5, 5, 5],
        "Math Operations": [5, 5, 5],
        "Project Management": [5, 5, 5],
        "Simple Chatbot": [5, 5, 5],
        "Student Record System": [5, 2.5, 4],
        "Text Analyser": [5, 5, 5],
    }
    
    # sets = {"Long Program": 5}

    for prog, vals in sets.items():
        for name in diff:
            temp = []
            folderPath = f"Datasets/{prog}/{name}"
            folderFiles = [
                file
                for file in os.listdir(folderPath)
                if not file.startswith(".DS_Store")
            ]

            for file in folderFiles:

                filePath1 = f"Datasets/{prog}/{name}/program_v1.py"
                filePath2 = os.path.join(folderPath, file)
                print(filePath2)
                # print(versionNumber)
                comp = ProgramDepTree()
                startTime = timeit.default_timer()
                pdg1 = comp.generatePdtFromFile(filePath1)
                pdg2 = comp.generatePdtFromFile(filePath2)
                res = comp.calculateSimilarity(pdg1, pdg2)
                res2 = comp.findBestMatchingElements(pdg1, pdg2)
                # print(res)
                endTime = timeit.default_timer()
                executionTime = endTime - startTime
                totalExecutionTime += executionTime

                numRuns += 1

    avgExecutionTime = totalExecutionTime / numRuns

    return avgExecutionTime


avgExecutionTimes = testing()
print("Average execution time:", avgExecutionTimes)
