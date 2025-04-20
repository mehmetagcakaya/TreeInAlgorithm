class Tree:
    def __init__(self, n):
        self.n = n
        self.node_names = []
        self.adjacency_List = {}
        self.adjacency_matrix = []

    def adding_nodes(self, nameof_node):
        nameof_node = nameof_node.lower()
        if nameof_node in self.node_names:
            print(f"Error: '{nameof_node}' already available!")
            return False

        self.node_names.append(nameof_node)
        self.adjacency_List[nameof_node] = []
        for row in self.adjacency_matrix:
            row.append(0)
        self.adjacency_matrix.append([0] * len(self.node_names))
        return True

    def inserting_elements(self, u, v):
        u, v = u.lower(), v.lower()
        if u not in self.node_names or v not in self.node_names:
            print("Error: Nodes do not exist!")
            return

        if u == v:
            print("Error:A node cannot establish a connection with itself!")
            return

        if v not in self.adjacency_List[u]:
            self.adjacency_List[u].append(v)
        if u not in self.adjacency_List[v]:
            self.adjacency_List[v].append(u)

        indxof_u = self.node_names.index(u)
        indxof_v = self.node_names.index(v)
        self.adjacency_matrix[indxof_u][indxof_v] = 1
        self.adjacency_matrix[indxof_v][indxof_u] = 1

    def delete_element(self, u, v):
        u, v = u.lower(), v.lower()
        if u in self.adjacency_List and v in self.adjacency_List[u]:
            self.adjacency_List[u].remove(v)
        if v in self.adjacency_List and u in self.adjacency_List[v]:
            self.adjacency_List[v].remove(u)

        indxof2_u = self.node_names.index(u)
        indxof2_v = self.node_names.index(v)
        self.adjacency_matrix[indxof2_u][indxof2_v] = 0
        self.adjacency_matrix[indxof2_v][indxof2_u] = 0

    def finding_elements(self, u, v):
        u, v = u.lower(), v.lower()
        indxof3_u = self.node_names.index(u)
        indxof3_v = self.node_names.index(v)
        return self.adjacency_matrix[indxof3_u][indxof3_v] == 1

    def printing_all(self):
        print("\nAdjacency List Representation:")
        for node, neighbors in self.adjacency_List.items():
            print(f"{node}: {neighbors}")

        print("\nAdjacency Matrix Representation:")
        print("   " + " ".join(self.node_names))
        for i, row in enumerate(self.adjacency_matrix):
            print(f"{self.node_names[i]}: " + " ".join(map(str, row)))


def creation_tree_from_user_stage():
    n = int(input("Please enter the number of nodes of the tree (n): "))
    our_tree = Tree(n)

    print("\nPlease enter unique names for the nodes:")
    for _ in range(n):
        while True:
            node_name = input(f"Node name (Total  {n} pieces, {len(our_tree.node_names) + 1}. node): ")
            if our_tree.adding_nodes(node_name):
                break

    print("\nCreating a tree. Enter the links for each node:")
    for node in our_tree.node_names:
        while True:
            print(f"For node '{node}' enter the connected nodes separated by a space (if there is no connection, just press Enter):")
            neighbours = input().strip()
            if neighbours:
                neighbours = neighbours.split()
                validation = True
                for neighbour in neighbours:
                    if neighbour.lower() == node:
                        print("Error: A node cannot connect with itself!")
                        validation = False
                        break
                    if neighbour.lower() not in our_tree.node_names:
                        print(f"Error: '{neighbour}' an invalid node name.")
                        validation = False
                        break
                if validation:
                    for neighbour in neighbours:
                        our_tree.inserting_elements(node, neighbour)
                    break
            else:
                break

    return our_tree


def tree_menu():
    print("\nSelect The Operation To Be Performed Below!:")
    print("1. Add Edge")
    print("2. Delete Edge")
    print("3. Find Edge")
    print("4. Print All Elements [Adjacency List and Adjacency Matrix representations]")
    print("5. Exit ")
    return int(input("Please Select An Action (1-5): "))


if __name__ == "__main__":
    tree = creation_tree_from_user_stage()

    while True:
        user_choice = tree_menu()

        if user_choice == 1:
            u, v = input("To add an edge, enter two node names (e.g. A B): ").split()
            tree.inserting_elements(u, v)
            print(f"Edge ({u.lower()}, {v.lower()}) added.")

        elif user_choice == 2:
            while True:
                try:
                    u, v = input("To delete an edge, enter two node names (e.g. A B): ").split()
                    tree.delete_element(u, v)
                    print(f"Edge ({u.lower()}, {v.lower()}) deleted.")
                    break
                except ValueError:
                    print("Error: Please enter two node names. Example: A B")

        elif user_choice == 3:
            u, v = input("Enter two node names to check for the presence of an edge (e.g. A B): ").split()
            exists = tree.finding_elements(u, v)
            print(f"Kenar ({u.lower()}, {v.lower()}) {'var' if exists else 'yok'}.")

        elif user_choice == 4:
            tree.printing_all()

        elif user_choice == 5:
            print("Ending the programme.")
            break

        else:
            print("Invalid selection! Please enter a number between 1-5.!")
