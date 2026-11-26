import os
import sys

def main():
    # The message must be strictly under 160 characters
    message = "All servers are down. The engineers are aware, and are currently googling the error message on the servers that are down."
    
    if len(message) >= 160:
        print("Error: Message exceeds 159 characters", file=sys.stderr)
        sys.exit(1)
        
    # Write to the make.fun grader's output directory
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(message)
        
    # Also print to stdout
    print(message)

if __name__ == "__main__":
    main()