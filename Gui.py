import TeamStatistics as ts
import Model as mdl
import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()

stats_class = ts.TeamStatistics()
stats_class.read_in_data()

class Application(tk.Frame):
    def __init__(self, master=root):
        master.minsize(400, 400)
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.calc_button = tk.Button(root, text='Calculate', command=self.display_results)
        self.calc_button.place(relx=.5, rely=.5, anchor=tk.CENTER)

        teams = ['Villanova', 'Kansas', 'North Carolina', 'Gonzaga', 'Kentucky', 'Arizona', 'Duke', 'Louisville',
                 'Oregon', 'Florida St.', 'UCLA', 'Baylor', 'Butler', 'Florida', 'West Virginia', 'Purdue', 'Virginia']

        self.team1_combo = ttk.Combobox(root)
        self.team1_combo.place(relx=.177, rely=.25, anchor=tk.CENTER)
        self.team1_combo['values'] = teams

        self.team2_combo = ttk.Combobox(root)
        self.team2_combo.place(relx=.823, rely=.25, anchor=tk.CENTER)
        self.team2_combo['values'] = teams

        self.team1_label = tk.Label(root, text='Team 1')
        self.team1_label.place(relx=.177, rely=.18, anchor=tk.CENTER)

        self.team2_label = tk.Label(root, text='Team 2')
        self.team2_label.place(relx=.823, rely=.18, anchor=tk.CENTER)

        self.vs_label = tk.Label(root, text='V.S.')
        self.vs_label.place(relx=.5, rely=.25, anchor=tk.CENTER)

        self.result1 = tk.Label(root, text='')
        self.result1.place(relx=.177, rely=.38, anchor=tk.CENTER)

        self.result2 = tk.Label(root, text='')
        self.result2.place(relx=.823, rely=.38, anchor=tk.CENTER)

    def display_results(self):
        #TODO FIX HARDCODE
        self.result1['text'] = "Villanova Probability: 73%"
        self.result2['text'] = "Duke Probability: 27%"


def main(args):
    app = Application(master=root)
    app.master.title('March Madness Predictor')

    app.mainloop()


if __name__ == "__main__":
    import sys
    main(sys.argv)