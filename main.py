import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import *
import os

from ProgramDependency import ProgramDepTree


LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)
SMALLFONT = ("Verdana", 12)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Python3 Plagiarism Detector")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MultiSelectPage, Page1, Page2, AnalysisPageResults):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(StartPage)

    def showFrame(
        self,
        cont,
        text=None,
        file1Contents=None,
        file2Contents=None,
        file1Path=None,
        file2Path=None,
    ):
        frame = self.frames[cont]
        if text is not None:
            frame.update_text(text)
        if file1Contents is not None:
            frame.displayFileContents(
                file1Contents=file1Contents,
                file2Contents=file2Contents,
                file1Path=file1Path,
                file2Path=file2Path,
            )
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        style = ttk.Style()
        style.configure("StartPage.TLabel", foreground="black")
        style.configure("StartPage.TButton", foreground="black")
        # style.configure("StartPage.TWelcome", foreground="black")

        label = ttk.Label(
            self,
            text="Python Plagiarism Detector (Program Dependency Trees)",
            font=LARGEFONT,
            style="StartPage.TLabel",
        )
        label.grid(row=0, column=4, padx=10, pady=10)

        howToUseText = """
            How to use:
            1. Select either option "Select Files" or "Compare against folder".
            2. Input selected files or selected folders.
            3. Press analyse/compare button.

            How to understand analyse results:
            The first text box will contain data regarding (code snippets from file 1) in the format match {No.}:
            node data. This will also be shown in the second text box which contains the data from file 2 in the same format
            match {No.}: node data. The third box then shows again the match{No.}: {Score%}

            Disclaimer: This system does not guarantee the detection of plagiarism or collusion. 
            It is designed to identify potential similarities in Python code. 
            The interpretation of results and any subsequent actions taken are the responsibility of the user. 
            Users should exercise judgment and critical thinking when analysing the output of this system.
        """

        howToUseLabel = ttk.Label(
            self,
            text=howToUseText,
            font=SMALLFONT,
            style="StartPage.TLabel",
        )
        howToUseLabel.grid(row=3, column=4, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="Select Files",
            command=lambda: controller.showFrame(Page1),
            style="StartPage.TButton",
        )
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="Compare Folder",
            command=lambda: controller.showFrame(MultiSelectPage),
            style="StartPage.TButton",
        )
        button2.grid(row=2, column=1, padx=10, pady=10)


class MultiSelectPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        style = ttk.Style()
        style.configure("MultiSelect.TLabel", foreground="black")
        style.configure("MultiSelect.TButton", foreground="black")
        style.configure("Treeview.Heading", foreground="black")

        self.selectedFile = None
        self.selectedFolder = None

        self.results = {}

        # Labels
        ttk.Label(self, text="Select Python File:", style="MultiSelect.TLabel").grid(
            row=0, column=0, padx=10, pady=5
        )
        ttk.Label(
            self, text="Select Folder of Python Files:", style="MultiSelect.TLabel"
        ).grid(row=1, column=0, padx=10, pady=5)

        # Text Entry for File Path
        self.fileEntry = tk.Entry(self, width=50, state="readonly")
        self.fileEntry.grid(row=0, column=1, padx=10, pady=5)

        # Button to Select Python File
        ttk.Button(
            self, text="Browse", command=self.selectFile, style="MultiSelect.TButton"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=5,
        )

        # Text Entry for Folder Path
        self.folderEntry = tk.Entry(self, width=50, state="readonly")
        self.folderEntry.grid(row=1, column=1, padx=10, pady=5)

        # Button to Select Folder
        ttk.Button(
            self, text="Browse", command=self.selectFolder, style="MultiSelect.TButton"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=5,
        )

        # Compare Button
        ttk.Button(
            self, text="Compare", command=self.compareFiles, style="MultiSelect.TButton"
        ).grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(
            self,
            text="Back",
            command=lambda: controller.showFrame(StartPage),
            style="MultiSelect.TButton",
        ).grid(row=2, column=0, padx=10, pady=10)

        # Treeview to display results
        self.resultsTree = ttk.Treeview(self, columns=("Score"), selectmode="browse")
        self.resultsTree.heading("#0", text="Program Name")
        self.resultsTree.heading("Score", text="Overall Score")
        self.resultsTree.column("Score", width=100, anchor="center")
        self.resultsTree.grid(row=3, columnspan=3, padx=10, pady=5, sticky="we")

        # Bind a function to handle the click event on the treeview
        self.resultsTree.bind("<ButtonRelease-1>", self.onTreeClick)

    def splitMatches(self, bestMatches):
        firstFileMatches = []
        secondFileMatches = []
        scores = []

        for match in bestMatches:
            firstFileMatches.append(match[0])
            secondFileMatches.append(match[1])
            scores.append(match[2])

        return firstFileMatches, secondFileMatches, scores

    def onTreeClick(self, event):
        # Get the item that was clicked
        itemId = self.resultsTree.selection()[0]
        itemText = self.resultsTree.item(itemId, "text")

        data = self.results[itemText]
        matches = data["Best Matches"]
        # print(f"data = {data}")

        # Split the best matches into separate lists
        self.firstFileMatches, self.secondFileMatches, self.scores = self.splitMatches(
            matches
        )
        # Show a pop-up with the clicked item text
        # popup = tk.Toplevel(self)
        # popup.title(f"{itemText}: {overall}")

        firstFileMatchesText = Text(
            self,
            height=30,
            width=50,
            background="white",
            foreground="black",
        )
        firstFileMatchesText.grid(row=5, column=0, padx=10, pady=10)

        secondFileMatchesText = Text(
            self,
            height=30,
            width=50,
            background="white",
            foreground="black",
        )
        secondFileMatchesText.grid(row=5, column=1, padx=10, pady=10)

        scoresFileMatchesText = Text(
            self,
            height=30,
            width=50,
            background="white",
            foreground="black",
        )
        scoresFileMatchesText.grid(row=5, column=2, padx=10, pady=10)
        # label.pack()

        # Display matches and scores in respective Text widgets
        for idx, match in enumerate(self.firstFileMatches):
            firstFileMatchesText.insert(END, f"Match {idx + 1}: {match}\n----------\n")

        for idx, match in enumerate(self.secondFileMatches):
            secondFileMatchesText.insert(END, f"Match {idx + 1}: {match}\n----------\n")

        for idx, score in enumerate(self.scores):
            scoresFileMatchesText.insert(
                END, f"Match {idx + 1}: Similarity Score {score*100:.2f}%\n----------\n"
            )

    def selectFile(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.selectedFile = file_path
            self.fileEntry.configure(state="normal")
            self.fileEntry.delete(0, "end")
            self.fileEntry.insert(0, file_path)
            self.fileEntry.configure(state="readonly")

    def selectFolder(self):
        folderPath = filedialog.askdirectory()
        if folderPath:
            self.selectedFolder = folderPath
            self.folderEntry.configure(state="normal")
            self.folderEntry.delete(0, "end")
            self.folderEntry.insert(0, folderPath)
            self.folderEntry.configure(state="readonly")

    def clearAll(self):
        for item in self.resultsTree.get_children():
            self.resultsTree.delete(item)

    def compareFiles(self):
        try:
            if self.selectedFile and self.selectedFolder:
                folderPath = self.selectedFolder
                selectedFilePath = self.selectedFile
                self.clearAll()
                # Get a list of all files in the selected folder
                folderFiles = [
                    file
                    for file in os.listdir(folderPath)
                    if not file.startswith(".DS_Store") and file.endswith(".py")
                ]
                # print(folderFiles)
                formattedResults = []

                resultsList = []

                for idx, fileName in enumerate(folderFiles):
                    # Construct the full path of the file
                    filePath2 = os.path.join(folderPath, fileName)

                    comp = ProgramDepTree()
                    pdg1 = comp.generatePdtFromFile(selectedFilePath)
                    pdg2 = comp.generatePdtFromFile(filePath2)
                    result = comp.calculateSimilarity(pdg1, pdg2)
                    bestMatches = comp.findBestMatchingElements(pdg1, pdg2)
                    self.results[os.path.basename(filePath2)] = {
                        "Overall": result,
                        "Best Matches": bestMatches,
                    }

                    # Format the result for printing
                    formattedResult = f"Program Name: {os.path.basename(filePath2)}\n"
                    formattedResult += f"Overall Score: {result}\n"
                    formattedResult += "Best Matches:\n"
                    for match in bestMatches:
                        formattedResult += f"  - {match}\n"

                    # Append the formatted result to the list
                    formattedResults.append(formattedResult)

                    resultsList.append((os.path.basename(filePath2), result))

                resultsList.sort(key=lambda x: x[1], reverse=True)
                for name, score in resultsList:
                    self.resultsTree.insert(
                        "",
                        "end",
                        text=name,
                        values=(f"{score*100:.2f}%",),
                    )

            else:
                messagebox.showerror(
                    "Please select a Python file and a folder of Python files.",
                )
        except Exception as e:
            errorMessage = f"Failed to analyse: {str(e)}"
            messagebox.showerror("Analysis Error", errorMessage)


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        style = ttk.Style()
        style.configure("Page1.TLabel", foreground="black")
        style.configure("StartPage.TButton", foreground="black", width=15, height=10)

        label = ttk.Label(
            self, text="Select Files", font=LARGEFONT, style="Page1.TLabel"
        )
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="Start Page",
            command=lambda: controller.showFrame(StartPage),
            style="StartPage.TButton",
        )
        button1.grid(row=1, column=1, padx=10, pady=10)

        self.file1Label = ttk.Label(self, text="", style="Page1.TLabel")
        self.file1Label.grid(row=2, column=3, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="Select First File",
            command=lambda: self.loadFirstFile(controller),
            style="StartPage.TButton",
        )
        button2.grid(row=2, column=1, padx=10, pady=10)

        self.file2Label = ttk.Label(self, text="", style="Page1.TLabel")
        self.file2Label.grid(row=3, column=3, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="Select Second File",
            command=lambda: self.loadSecondFile(controller),
            style="StartPage.TButton",
        )
        button3.grid(row=3, column=1, padx=10, pady=10)

        self.page2Button = ttk.Button(
            self,
            text="Submit",
            command=lambda: self.loadPage2(controller),
            style="StartPage.TButton",
            state=tk.DISABLED,  # Initially disabled until both files are selected
        )
        self.page2Button.grid(row=4, column=1, padx=10, pady=10)

        self.file1Contents = None
        self.file2Contents = None

        self.file1Path = None
        self.file2Path = None

    def loadFirstFile(self, controller):
        filePath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if filePath:
            self.file1Path = filePath
            self.file1Label.config(text=f"Selected File: {os.path.basename(filePath)}")
            with open(filePath, "r") as file:
                self.file1Contents = file.read()
                if self.file2Contents is not None:  # Check if both files are selected
                    self.page2Button["state"] = tk.NORMAL

    def loadSecondFile(self, controller):
        filePath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if filePath:
            self.file2Label.config(text=f"Selected File: {os.path.basename(filePath)}")
            self.file2Path = filePath
            with open(filePath, "r") as file:
                self.file2Contents = file.read()
                if self.file1Contents is not None:  # Check if both files are selected
                    self.page2Button["state"] = tk.NORMAL

    def loadPage2(self, controller):
        if self.file1Contents is not None and self.file2Contents is not None:
            page = controller.frames[Page2]
            page.clearTextAreas()
            controller.showFrame(
                Page2,
                file1Contents=self.file1Contents,
                file2Contents=self.file2Contents,
                file1Path=self.file1Path,
                file2Path=self.file2Path,
            )


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # self.loadAnalysisPage = False
        self.file1Contents = None
        self.file2Contents = None
        self.file1Path = None
        self.file2Path = None

        style = ttk.Style()
        style.configure("Page2.TLabel", foreground="black")

        self.label1 = ttk.Label(
            self, text="File 1 Contents", font=LARGEFONT, style="Page2.TLabel"
        )
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.textArea1 = Text(
            self,
            height=10,
            width=50,
            background="white",
            foreground="black",
        )
        self.textArea1.grid(row=1, column=0, padx=10, pady=10)

        self.label2 = ttk.Label(
            self, text="File 2 Contents", font=LARGEFONT, style="Page2.TLabel"
        )
        self.label2.grid(row=0, column=1, padx=10, pady=10)

        self.textArea2 = Text(
            self,
            height=10,
            width=50,
            background="white",
            foreground="black",
        )
        self.textArea2.grid(row=1, column=1, padx=10, pady=10)

        self.textArea3 = Text(
            self,
            height=10,
            width=50,
            background="white",
            foreground="black",
        )
        self.textArea3.grid(row=3, column=0, padx=10, pady=10)

        self.textArea4 = Text(
            self,
            height=10,
            width=50,
            background="white",
            foreground="black",
        )
        self.textArea4.grid(row=3, column=1, padx=10, pady=10)

        button1 = ttk.Button(
            self,
            text="Home Page",
            command=lambda: controller.showFrame(StartPage),
            style="StartPage.TButton",
        )
        button1.grid(row=5, column=0, padx=10, pady=10)

        analyseButton = ttk.Button(
            self,
            text="Analyse",
            command=lambda: self.loadAnalysePage(controller),
            style="StartPage.TButton",
        )
        analyseButton.grid(row=5, column=1, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="Reselect Files",
            command=lambda: controller.showFrame(Page1),
            style="StartPage.TButton",
        )
        button2.grid(row=5, column=3, padx=10, pady=10)

    def clearTextAreas(self):
        self.textArea1.delete("1.0", END)
        self.textArea2.delete("1.0", END)
        self.textArea3.delete("1.0", END)
        self.textArea4.delete("1.0", END)

    def displayFileContents(
        self, file1Contents=None, file2Contents=None, file1Path=None, file2Path=None
    ):
        if file1Contents is not None:
            self.textArea1.insert(END, file1Contents)
            self.file1Contents = file1Contents

        if file2Contents is not None:
            self.textArea2.insert(END, file2Contents)
            self.file2Contents = file2Contents

        if file1Path is not None:
            self.textArea3.insert(END, file1Path)
            self.file1Path = file1Path

        if file2Path is not None:
            self.textArea4.insert(END, file2Path)
            self.file2Path = file2Path

    def analyse(self, file1_path, file2_path):
        comp = ProgramDepTree()
        pdt1 = comp.generatePdtFromFile(file1_path)
        pdt2 = comp.generatePdtFromFile(file2_path)
        result = comp.calculateSimilarity(pdt1, pdt2)

        bestMatches = comp.findBestMatchingElements(pdt1, pdt2)
        # print(f"Similarity between {file1_path} and {file2_path} is: {result}")
        # for match in bestMatches:
        #    print(f"{match}")
        return result, bestMatches

    def loadAnalysePage(self, controller):
        try:
            result, bestMatches = self.analyse(self.file1Path, self.file2Path)
            # print(f"Analysis Result: {result}, Best Matches: {bestMatches}")  # Debug print
            page = controller.frames[AnalysisPageResults]
            page.setAnalysisResults(result, bestMatches)
            controller.showFrame(AnalysisPageResults)
        except Exception as e:
            errorMessage = f"Failed to analyse: {str(e)}"
            messagebox.showerror("Analysis Error", errorMessage)


class AnalysisPageResults(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.results = None
        self.bestMatches = None
        self.firstFileMatches = None
        self.secondFileMatches = None
        self.scores = None

        style = ttk.Style()
        style.configure("Page2.TLabel", foreground="black")
        style.configure("StartPage.TButton", foreground="black")

        self.resultLabel = ttk.Label(
            self, text="Overall Similarity Score: ", style="Page2.TLabel"
        )
        self.resultLabel.grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Label(self, text="First File Matches", style="Page2.TLabel").grid(
            row=1, column=0, padx=10
        )
        ttk.Label(self, text="Second File Matches", style="Page2.TLabel").grid(
            row=1, column=1, padx=10
        )
        ttk.Label(self, text="Scores", style="Page2.TLabel").grid(
            row=1, column=2, padx=10
        )

        button1 = ttk.Button(
            self,
            text="Back",
            command=lambda: controller.showFrame(Page2),
            style="StartPage.TButton",
        )
        button1.grid(row=7, column=0, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="Reselect Files",
            command=lambda: controller.showFrame(Page1),
            style="StartPage.TButton",
        )
        button2.grid(row=7, column=1, padx=10, pady=10)

        self.firstFileMatchesText = Text(
            self,
            height=30,
            width=50,
            background="white",
            foreground="black",
        )
        self.firstFileMatchesText.grid(row=2, column=0, padx=10, pady=10)

        self.secondFileMatchesText = Text(
            self,
            height=30,
            width=50,
            background="white",
            foreground="black",
        )
        self.secondFileMatchesText.grid(row=2, column=1, padx=10, pady=10)

        self.scoresFileMatchesText = Text(
            self,
            height=30,
            width=50,
            background="white",
            foreground="black",
        )
        self.scoresFileMatchesText.grid(row=2, column=2, padx=10, pady=10)

    def setAnalysisResults(self, result, bestMatches):
        # Update the result label
        self.resultLabel.config(text=f"Overall Similarity Score: {result*100:.2f}%")

        # Clear previous matches
        self.firstFileMatchesText.delete("1.0", END)
        self.secondFileMatchesText.delete("1.0", END)
        self.scoresFileMatchesText.delete("1.0", END)

        # Split the best matches into separate lists
        self.firstFileMatches, self.secondFileMatches, self.scores = self.splitMatches(
            bestMatches
        )

        # Display matches and scores in respective Text widgets
        for idx, match in enumerate(self.firstFileMatches):
            self.firstFileMatchesText.insert(
                END, f"Match {idx + 1}: {match}\n----------\n"
            )

        for idx, match in enumerate(self.secondFileMatches):
            self.secondFileMatchesText.insert(
                END, f"Match {idx + 1}: {match}\n----------\n"
            )

        for idx, score in enumerate(self.scores):
            self.scoresFileMatchesText.insert(
                END, f"Match {idx + 1}: Similarity Score {score*100:.2f}%\n----------\n"
            )

    def splitMatches(self, bestMatches):
        firstFileMatches = []
        secondFileMatches = []
        scores = []

        for match in bestMatches:
            firstFileMatches.append(match[0])
            secondFileMatches.append(match[1])
            scores.append(match[2])

        return firstFileMatches, secondFileMatches, scores

    def clearTextAreas(self):
        self.resultLabel.config(text="Similarity Score: ")
        self.firstFileMatchesText.delete("1.0", END)
        self.secondFileMatchesText.delete("1.0", END)
        self.scoresFileMatchesText.delete("1.0", END)


app = tkinterApp()
app.mainloop()
