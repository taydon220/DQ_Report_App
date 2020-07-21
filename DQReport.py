import os
import pandas


def remove_extra_stuff(filename, columns_to_keep, report_type):
    try:
        print("_______________________________________________________")
        data_frame = pandas.read_csv(f'./unedited/{filename}')
        trimmed_df = data_frame[columns_to_keep]  # data_frame[[]] list of lists makes it use only those columns
        if report_type == '1':  # PODQ report; Renames columns. Gets rid of "Custom Field" part.
            trimmed_df.columns = ["Summary", "Vendor", "Reporter", "Status", "Created",
                                  "Resolved", "Product Type", "SOS PN"]
            trimmed_df.insert(6, "Resolve Time", value="")  # Adds column titled "Resolve Time" with blank values.
            trimmed_df.to_csv(f'./edited/EDIT_{filename}', index=False)

            print("Converting trimmed data frame to csv.")
            print(f"SUCCESS! 'EDIT_{filename}' created.")
            print(f"There were {len(trimmed_df)} PODQs last month.")
            return

        elif report_type == '2':  # SODQ report; Renames columns. Gets rid of "Custom Field" part.
            trimmed_df.columns = ["Summary", "Created", "Resolved", "Customer", "Product Type",
                                  "Return Reason", "SOS PN", "Test Result"]
            trimmed_df.insert(3, "Resolve Time", value="")  # Adds column titled "Resolve Time" with blank values.
            trimmed_df.to_csv(f'./edited/EDIT_{filename}', index=False)

            print("Converting trimmed data frame to csv.")
            print(f"SUCCESS! 'EDIT_{filename}' created.")
            print(f"There were {len(trimmed_df)} SODQs last month.")
            return

    except pandas.errors.EmptyDataError or KeyError or ValueError or IOError:
        print("ERROR!! There was an issue with the file.")
        exit()


def menu():
        print("Welcome to the Daily Question Report Generator.", "\n")
        print("For a PODQ Report, press (1)")
        print("For an SODQ Report, press (2)")
        # print("For a NET PODQ Report, press (3)")
        print("Press (q) to quit.", "\n")
        answer = input(" ")
        if answer.lower() not in ["1", "2", "q", "test"]:
            menu()
        return answer.lower()


def main():
    while True:
        print("_______________________________________________________")
        type_of_report = menu()
        if type_of_report == 'q':
            exit()
        target_file = input("Filename to remove extra columns from (include .csv at the end): ")
        possible_file_names = [x.lower() for x in os.listdir("unedited")]
        if not target_file.endswith(".csv") or target_file.lower() not in possible_file_names:
            print("\nFile not found!", "\n")
            main()

        if type_of_report == '1':  # Reorders and keeps what's needed for Google Drive template.
            info_to_keep = ["Summary", "Custom field (Vendor)", "Reporter", "Status", "Created", "Resolved",
                            "Custom field (Product Type)", "Custom field (SOS PN)"]

        elif type_of_report == '2':
            info_to_keep = ["Summary", "Created", "Resolved", "Custom field (Customer)", "Custom field (Product Type)",
                            "Custom field (Return Reason)", "Custom field (SOS PN)", "Custom field (Test Result)"]

        else:
            exit()

        remove_extra_stuff(target_file, info_to_keep, type_of_report)

if __name__ == "__main__":
    os.makedirs('edited', exist_ok=True)
    main()
