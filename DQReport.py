import os
import pandas


def remove_extra_stuff(filename, columns_to_keep, report_type):
    try:
        data_frame = pandas.read_csv(f'./unedited/{filename}')
        trimmed_df = data_frame[columns_to_keep]  # data_frame[[]] list of lists makes it use only those columns

        if report_type == '1':  # PODQ report
            trimmed_df.columns = ["Summary", "Vendor", "Reporter", "Status", "Created", "Resolved",
                                  "Product Type", "SOS PN"]
            trimmed_df.insert(6, "Resolve Time", value="")
            podq_total = len(trimmed_df)
            additional_data = pandas.DataFrame({"Summary": [""], "Vendor": [""], "Reporter": [""], "Status": [""],
                                                "Created": [""], "Resolved": [""], "Product Type": [""], "SOS PN": [""],
                                                "J": [""], "K": [""], "L": [""], "M": [""],
                                                f"Total = {podq_total}": [""]})

            completed_df = trimmed_df.append(additional_data, sort=False)
            completed_df.to_csv(f'./edited/EDIT_{filename}', index=False)
            # trimmed_df.to_csv(f'./edited/TEST_{filename}', index=False)
            print("SUCCESS!")
            return

        elif report_type == '2':  # SODQ report
            trimmed_df.columns = ["Summary", "Created", "Resolved", "Customer", "Product Type",
                                  "Return Reason", "SOS PN", "Test Result"]
            trimmed_df.insert(3,"Resolve Time", value="")
            sodq_total = len(trimmed_df)
            additional_data = pandas.DataFrame({"Summary": [""], "Created": [""], "Resolved": [""],
                                                "Customer": [""], "Product Type": [""], "Return Reason": [""],
                                                "SOS PN": [""], "Test Result": [""]})

            completed_df = trimmed_df.append(additional_data, sort=False)
            completed_df.to_csv(f'./edited/EDIT_{filename}', index=False)
            print("SUCCESS!")
            return

        elif report_type == 'test':
            return

    except pandas.errors.EmptyDataError or KeyError or ValueError:
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
        type_of_report = menu()
        if type_of_report == 'q':
            exit()
        target_file = input("Filename to remove extra columns from (include .csv at the end): ")
        possible_file_names = [x.lower() for x in os.listdir("unedited")]
        if not target_file.endswith(".csv") or target_file.lower() not in possible_file_names:
            print("\nFile not found!", "\n")
            main()

        if type_of_report == '1':
            info_to_keep = ["Summary", "Created", "Status", "Reporter", "Resolved", "Custom field (Product Type)",
                            "Custom field (Vendor)", "Custom field (SOS PN)"]

        elif type_of_report == '2':
            info_to_keep = ["Summary", "Created", "Resolved", "Custom field (Customer)", "Custom field (Product Type)",
                            "Custom field (Return Reason)", "Custom field (SOS PN)", "Custom field (Test Result)"]

        elif type_of_report == 'test':
            info_to_keep = ["Summary", "Custom field (Vendor)", "Reporter", "Status", "Created",
                            "Resolved", "Custom field (Product Type)", "Custom field (SOS PN)"]

        else:
            exit()

        remove_extra_stuff(target_file, info_to_keep, type_of_report)

if __name__ == "__main__":
    os.makedirs('edited', exist_ok=True)
    main()
