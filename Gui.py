import TeamStatistics as ts
import Model as mdl
import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()


stats_class = ts.TeamStatistics()
stats_class.read_in_data()
model = mdl.Model()

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
                 'Oregon', 'Florida St', 'UCLA', 'Baylor', 'Butler', 'Florida', 'West Virginia', 'Purdue', 'Virginia']

        years = [2008, 2009, 2010, 2011, 2012, 2013, 2014]

        self.year_label = tk.Label(root, text='Year:')
        self.year_label.place(relx=.5, rely=.03, anchor=tk.CENTER)

        self.year_combo = ttk.Combobox(root)
        self.year_combo.place(relx=.5, rely=.1, anchor=tk.CENTER)
        self.year_combo['values'] = years

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

        self.result = tk.Label(root, text='')
        self.result.place(relx=.5, rely=.38, anchor=tk.CENTER)

    def display_results(self):
        team1_name = self.team1_combo.get()
        team2_name = self.team2_combo.get()
        year = int(self.year_combo.get())
        stats_class.populate_game_stats(team1_name, year)
        stats_class.create_stats(team1_name, year)
        stats_class.populate_game_stats(team2_name, year)
        stats_class.create_stats(team2_name, year)

        result = model.predict_winner(stats_class.season_averages[team1_name, year], stats_class.season_averages[team2_name, year])

        if result == True:
            self.result['text'] = team1_name + " is predicted to win."
        else:
            self.result['text'] = team2_name + " is predicted to win."






def main(args):
    app = Application(master=root)
    app.master.title('March Madness Predictor')

    app.mainloop()


if __name__ == "__main__":
    import sys
    main(sys.argv)