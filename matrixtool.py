#!/usr/bin/env python3
import numpy as np

def format_elem(x):
    from math import isclose
    try:
        if isclose(x, round(x), rel_tol=1e-9, abs_tol=1e-9):
            return str(int(round(x)))
        else:
            return f"{x:.4f}"
    except Exception:
        return str(x)

def pretty_print_matrix(A, title=None):
    A = np.asarray(A)
    if A.ndim != 2:
        print("Not a 2D matrix.")
        return
    rows, cols = A.shape
    table = [[format_elem(A[i, j]) for j in range(cols)] for i in range(rows)]
    col_widths = [max(len(table[i][j]) for i in range(rows)) for j in range(cols)]
    if title:
        print(title)
    sep = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
    print(sep)
    for i in range(rows):
        row_str = " | ".join(table[i][j].rjust(col_widths[j]) for j in range(cols))
        print(f"| {row_str} |")
        print(sep)
    print()

def input_matrix_cli(name="Matrix"):
    while True:
        try:
            rows = int(input(f"Enter number of rows for {name}: ").strip())
            cols = int(input(f"Enter number of columns for {name}: ").strip())
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue
            break
        except ValueError:
            print("Please enter valid integers for rows and columns.")
    print(f"Enter each row of {name} as space-separated numbers (total {cols} values per row):")
    data = []
    for r in range(rows):
        while True:
            row_input = input(f"Row {r+1}: ").strip().split()
            if len(row_input) != cols:
                print(f"Expected {cols} values but got {len(row_input)}. Try again.")
                continue
            try:
                row = [float(x) for x in row_input]
            except ValueError:
                print("Non-numeric value entered. Try again.")
                continue
            data.append(row)
            break
    return np.array(data)

def add_matrices(A, B):
    if A.shape != B.shape:
        raise ValueError("Addition requires matrices of the same shape.")
    return A + B

def subtract_matrices(A, B):
    if A.shape != B.shape:
        raise ValueError("Subtraction requires matrices of the same shape.")
    return A - B

def multiply_matrices(A, B):
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("Both inputs must be 2D matrices.")
    if A.shape[1] != B.shape[0]:
        raise ValueError("Inner dimensions must match for multiplication.")
    return A.dot(B)

def transpose_matrix(A):
    return A.T

def determinant(A):
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Determinant requires a square matrix.")
    return float(np.linalg.det(A))

def main():
    print("Matrix Operations Tool (CLI)")
    print("============================")
    A = None
    B = None
    while True:
        print("\nOptions:")
        print("1) Input Matrix A")
        print("2) Input Matrix B")
        print("3) Add A + B")
        print("4) Subtract A - B")
        print("5) Multiply A x B")
        print("6) Transpose A or B")
        print("7) Determinant of A or B")
        print("8) Show current matrices")
        print("9) Exit")
        choice = input("Choose an option (1-9): ").strip()
        try:
            if choice == "1":
                A = input_matrix_cli("Matrix A")
            elif choice == "2":
                B = input_matrix_cli("Matrix B")
            elif choice == "3":
                if A is None or B is None:
                    print("Please define both matrices first (options 1 and 2).")
                else:
                    pretty_print_matrix(add_matrices(A, B), title="A + B:")
            elif choice == "4":
                if A is None or B is None:
                    print("Please define both matrices first.")
                else:
                    pretty_print_matrix(subtract_matrices(A, B), title="A - B:")
            elif choice == "5":
                if A is None or B is None:
                    print("Please define both matrices first.")
                else:
                    pretty_print_matrix(multiply_matrices(A, B), title="A x B:")
            elif choice == "6":
                which = input("Transpose which matrix (A/B)? ").strip().upper()
                if which == "A":
                    if A is None: print("Matrix A not defined."); continue
                    pretty_print_matrix(transpose_matrix(A), title="A^T:")
                else:
                    if B is None: print("Matrix B not defined."); continue
                    pretty_print_matrix(transpose_matrix(B), title="B^T:")
            elif choice == "7":
                which = input("Determinant of which (A/B)? ").strip().upper()
                if which == "A":
                    if A is None: print("Matrix A not defined."); continue
                    print("det(A) =", determinant(A))
                else:
                    if B is None: print("Matrix B not defined."); continue
                    print("det(B) =", determinant(B))
            elif choice == "8":
                print("Current Matrices:")
                if A is None:
                    print("Matrix A not defined.")
                else:
                    pretty_print_matrix(A, title="A")
                if B is None:
                    print("Matrix B not defined.")
                else:
                    pretty_print_matrix(B, title="B")
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Enter 1-9.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

