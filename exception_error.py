def divide_numbers(a, b):
    return a / b

def access_list_item(lst, index):
    return lst[index]

def convert_to_int(value):
    return int(value)

def demo_exception_handling():
    data = [1, 2, 3]

    test_cases = [
        (10, 0),      # ZeroDivisionError
        (10, "a"),    # TypeError
        (10, 2),      # No error
    ]

    for a, b in test_cases:
        try:
            print(f"\nTrying: {a} / {b}")
            result = divide_numbers(a, b)
            print(f"Result: {result}")

            print(f"Accessing list index: {b}")
            item = access_list_item(data, b if isinstance(b, int) else 0)
            print(f"List item: {item}")

            print(f"Converting '{b}' to int")
            num = convert_to_int(b)
            print(f"Converted: {num}")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except TypeError as e:
            print(f"Error: Type mismatch - {e}")
        except IndexError:
            print("Error: List index out of range.")
        except ValueError:
            print("Error: Invalid value, cannot convert to int.")
        except Exception as e:
            # Catch-all for anything unexpected
            print(f"Unexpected error: {type(e).__name__} - {e}")
        else:
            # Runs only if no exception occurred
            print("All operations completed successfully.")
        finally:
            # Always runs, exception or not
            print("Finished processing this test case.")

if __name__ == "__main__":
    demo_exception_handling()