#!/usr/bin/python3
import sys

def print_metrics(metrics):
    total_size = metrics.get("total_size", 0)
    status_codes = metrics.get("status_codes", {})
    
    print(f"Total file size: {total_size}")
    
    for status_code in sorted(status_codes.keys()):
        count = status_codes[status_code]
        print(f"{status_code}: {count}")

def main():
    metrics = {"total_size": 0, "status_codes": {}}
    line_count = 0
    
    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            
            if len(parts) >= 9:
                status_code = parts[8]
                file_size = int(parts[9])
                
                metrics["total_size"] += file_size
                if status_code in metrics["status_codes"]:
                    metrics["status_codes"][status_code] += 1
                else:
                    metrics["status_codes"][status_code] = 1
                
                if line_count % 10 == 0:
                    print_metrics(metrics)
    
    except KeyboardInterrupt:
        print_metrics(metrics)

if __name__ == "__main__":
    main()
