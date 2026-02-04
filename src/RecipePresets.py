import sqlite3
class RecipePresets:
    def __init__(self):
        # Declare presets as an empty dictionary, intended to hold keys of this form:
        # recipes = {
        #     "chili": [
        #         (60, 90),
        #         (120, 85),
        #         (30, 95),
        #     ],
        #     "yogurt": [
        #         (480, 43),
        #     ]
        self.presets: dict[str, list[tuple[int, int]]] = []
        self.load_presets()

    def get_preset(self):
        return self.presets
    
    def add_preset(self, name, intervals):
        #self.presets.append(dict["name": name, "times_temp": intervals])
        sql_insert_query = """
            INSERT INTO recipe_presets (name, order, length, temperature)
            VALUES (?, ?, ?, ?)
            """
        self.presets[name] = intervals
        con = sqlite3.connect("slow_cooker.db")
        cur = con.cursor

        # cur.execute(
        #     """
        #     SELECT name, "order", length, temperature
        #     FROM recipe_presets
        #     WHERE name = ?
        #     ORDER BY "order" DESC
        #     LIMIT 1
        #     """,
        #     (name,)
        # )
        # cur_order = cur.fetchone()[1]
        i = 1
        for row in intervals:
            cur.execute(sql_insert_query, (name, i, row[0], row[1]))
            i = i + 1
        con.commit
        con.close()


    def load_presets(self):
        con = sqlite3.connect("slow_cooker.db")
        cur = con.cursor

        cur.execute("" \
        "CREATE TABLE IF NOT EXISTS recipe_presets (" \
        "name TEXT," \
        "order INTEGER," \
        "length INTEGER," \
        "temperature INTEGER," \
        "PRIMARY KEY (name, order)" \
        ");")
        con.commit

        for row in cur.execute("SELECT * FROM recipe_presets;"):
            if not dict.__contains__(row[0]):
                self.presets[row[0]] = []
            self.presets[row[0]].append((row[2], row[3]))
        con.close()