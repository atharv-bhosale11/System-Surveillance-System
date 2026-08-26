# System Surveillance System
# Monitors CPU, RAM, Disk, Network, and Running Processes
# Generates timestamped log files periodically

import psutil
import sys
import os
import time
import schedule


def process_scan():
    process_list = []

    # Warm up CPU usage collection
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except Exception:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(
                attrs=[
                    "pid",
                    "name",
                    "username",
                    "status",
                    "create_time"
                ]
            )

            try:
                info["create_time"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.localtime(info["create_time"])
                )
            except Exception:
                info["create_time"] = "N/A"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            process_list.append(info)

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return process_list

def create_log(folder_name):

    border = "-" * 60

    if os.path.exists(folder_name):
        if not os.path.isdir(folder_name):
            print("Error: Specified path is not a directory.")
            return
    else:
        os.makedirs(folder_name)
        print("Log directory created successfully.")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    file_name = os.path.join(
        folder_name,
        f"SystemReport_{timestamp}.log"
    )

    print("Log file created:", file_name)

    with open(file_name, "w") as fobj:

        fobj.write(border + "\n")
        fobj.write("      SYSTEM SURVEILLANCE SYSTEM\n")
        fobj.write(border + "\n")
        fobj.write("Log Created At : " + time.ctime() + "\n")
        fobj.write(border + "\n\n")

        # CPU
        fobj.write("CPU Usage : %.2f %%\n" % psutil.cpu_percent())
        fobj.write(border + "\n")

        # RAM
        memory = psutil.virtual_memory()
        fobj.write("RAM Usage : %.2f %%\n" % memory.percent)
        fobj.write(border + "\n")

        # Disk Usage
        fobj.write("DISK USAGE REPORT\n")
        fobj.write(border + "\n")

        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)

                fobj.write(
                    "%s -> %.2f %% used\n"
                    % (partition.mountpoint, usage.percent)
                )

            except Exception:
                pass

        fobj.write(border + "\n")

        # Network Usage
        net = psutil.net_io_counters()

        fobj.write("NETWORK USAGE REPORT\n")
        fobj.write(border + "\n")

        fobj.write(
            "Data Sent     : %.2f MB\n"
            % (net.bytes_sent / (1024 * 1024))
        )

        fobj.write(
            "Data Received : %.2f MB\n"
            % (net.bytes_recv / (1024 * 1024))
        )

        fobj.write(border + "\n")

        # Process Information
        fobj.write("RUNNING PROCESS REPORT\n")
        fobj.write(border + "\n")

        process_data = process_scan()

        for info in process_data:

            fobj.write(f"PID          : {info.get('pid')}\n")
            fobj.write(f"Name         : {info.get('name')}\n")
            fobj.write(f"User         : {info.get('username')}\n")
            fobj.write(f"Status       : {info.get('status')}\n")
            fobj.write(f"Start Time   : {info.get('create_time')}\n")
            fobj.write(
                f"CPU Usage    : {info.get('cpu_percent'):.2f}%\n"
            )
            fobj.write(
                f"Memory Usage : {info.get('memory_percent'):.2f}%\n"
            )

            fobj.write(border + "\n")

        fobj.write("\n")
        fobj.write(border + "\n")
        fobj.write("END OF LOG FILE\n")
        fobj.write(border + "\n")


def main():

    border = "-" * 60

    print(border)
    print("      SYSTEM SURVEILLANCE SYSTEM")
    print(border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:

            print("This project performs:")
            print("1. CPU Monitoring")
            print("2. RAM Monitoring")
            print("3. Disk Monitoring")
            print("4. Network Monitoring")
            print("5. Process Monitoring")
            print("6. Automatic Log Generation")
            print("7. Scheduled Execution")

        elif sys.argv[1] in ["--u", "--U"]:

            print("Usage:")
            print("python system_surveillance.py Interval FolderName")
            print()
            print("Interval   : Time in minutes")
            print("FolderName : Log storage directory")

        else:

            print("Invalid option.")
            print("Use --h or --u")

    elif len(sys.argv) == 3:

        interval = int(sys.argv[1])
        folder_name = sys.argv[2]

        print("System Surveillance Started")
        print("Log Directory :", folder_name)
        print("Interval      :", interval, "minute(s)")
        print("Press CTRL + C to stop")

        schedule.every(interval).minutes.do(
            create_log,
            folder_name
        )

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:

        print("Invalid command line arguments.")
        print("Use --h or --u")

    print(border)
    print("Thank you for using System Surveillance System")
    print(border)


if __name__ == "__main__":
    main()
