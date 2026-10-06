# Trash Filtering Program
# Uses:
# - 2D Array/List
# - Class
# - Object
# - File reading
# - Dictionary


class TrashItem:
    def __init__(self, name, category, bin_index):
        self.name = name
        self.category = category
        self.bin_index = bin_index

    def show(self):
        print(
            self.name,
            "->",
            self.category,
            "(bin", self.bin_index + 1, ")"
        )


class TrashBin:
    def __init__(self, index, category):
        self.index = index
        self.category = category
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_count(self):
        return len(self.items)

    def get_summary(self):
        return (
            "Bin " + str(self.index + 1)
            + " (" + self.category + "): "
            + str(self.get_count())
            + " items"
        )


# -------------------------
# Read data from file
# -------------------------

def load_file(filename):

    # 2D Array/List
    data = []

    try:
        with open(filename, "r", encoding="utf-8") as file:

            for line in file:

                # Remove spaces and \n
                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                # Split by comma
                parts = line.split(",")

                # Our file has 2 pieces:
                # name, category
                if len(parts) >= 2:

                    name = parts[0].strip()
                    category = parts[1].strip().lower()

                    # Add row to 2D array
                    data.append([
                        name,
                        category
                    ])

    except FileNotFoundError:
        print("Error: File not found.")

    return data


# -------------------------
# Create TrashItem objects
# -------------------------

def create_objects(data, bin_map):

    items = []

    for row in data:

        name = row[0]
        category = row[1]

        # Automatically find the correct bin
        if category in bin_map:

            bin_index = bin_map[category]

            # Create object
            item = TrashItem(
                name,
                category,
                bin_index
            )

            # Add object to list
            items.append(item)

    return items


# -------------------------
# Main Program
# -------------------------

# Read trash.txt
data = load_file("improved_trash.txt")


# Create bins
bins = [
    TrashBin(0, "Recycle"),
    TrashBin(1, "General Waste"),
    TrashBin(2, "Organic Waste")
]


# Dictionary
# Category -> Bin number
bin_map = {
    "glass": 0,
    "plastic": 0,
    "paper": 0,
    "metal": 0,

    "food": 2
}


# Create TrashItem objects
trash_items = create_objects(data, bin_map)


# Put every item into its correct bin
for item in trash_items:

    bins[item.bin_index].add_item(item)


# -------------------------
# Print result
# -------------------------

print("===== TRASH SORTING RESULT =====")

for bin in bins:

    print()
    print(bin.get_summary())

    for item in bin.items:
        print(" - ", end="")
        item.show()
