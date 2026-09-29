# Trash Filtering Program
# Uses:
# - 2D Array/List
# - Class
# - Object
# - File reading

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


# Read data from file
def load_file(filename):

    # This is our 2D array
    data = []

    try:
        with open(filename, "r", encoding="utf-8") as file:

            for line in file:

                # Remove spaces and \n
                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                # Split the line by comma
                parts = line.split(",")

                # Make sure there are 3 pieces of data
                if len(parts) >= 3:

                    name = parts[0].strip()
                    category = parts[1].strip().lower()
                    bin_index = int(parts[2].strip())

                    # Add a row to the 2D array
                    data.append([
                        name,
                        category,
                        bin_index
                    ])

    except FileNotFoundError:
        print("Error: File not found.")

    return data


# Create TrashItem objects
def create_subclass(data):

    items = []

    # Go through every row in the 2D array
    for row in data:

        if len(row) == 3:

            # Create an object
            item = TrashItem(
                row[0],
                row[1],
                row[2]
            )

            # Add object to list
            items.append(item)

    return items


# Find the correct bin
def get_bin(category, bins):

    # Check every bin
    for bin in bins:

        if bin.category == category:
            return bin.index

    # If category doesn't exist
    return -1


# -------------------------
# Main Program
# -------------------------

# Read trash.txt
data = load_file("trash.txt")

# Create TrashItem objects
trash_items = create_subclass(data)

# Create TrashBin objects
bins = [
    TrashBin(0, "plastic"),
    TrashBin(1, "paper"),
    TrashBin(2, "metal")
]


# Put every trash item into its correct bin
for item in trash_items:

    bin_index = get_bin(item.category, bins)

    if bin_index != -1:
        bins[bin_index].add_item(item)


# Print the result
print("===== TRASH SORTING RESULT =====")

for bin in bins:

    print()
    print(bin.get_summary())

    for item in bin.items:
        print(" - ", end="")
        item.show()
