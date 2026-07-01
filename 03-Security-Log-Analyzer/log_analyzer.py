def log_analysis():
    file_path=input("Enter the file path of the Log\n")             # submit the log path

    checks = {
         "info" : 0,                                                # various parameters of log analysis
         "warning" : 0, 
        "error" : 0
    }
    try:
        with open(file_path) as info_file:
            lines=info_file.readlines()                            # to check if the file is present in the provided path, and take its contents as a list.
    except FileNotFoundError:
        print("FILE NOT FOUND")                                    # handling when the file is not found
        return
    for messages in lines :
        if "INFO" in messages:
            checks["info"] += 1

        if "WARNING"in messages:
            checks["warning"] += 1
        if "ERROR"in messages:
            checks["error"]  += 1

    print("===== LOG ANALYSIS REPORT =====")
    print(f"INFO MESSAGES : {checks.get('info')}")
    print(f"WARNING MESSAGES : {checks.get('warning')}")           # summary formatting
    print(f"ERROR MESSAGES : {checks.get('error')}")


log_analysis()                                                     # calling out the log anaylis funcitons
