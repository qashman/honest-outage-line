# main.py
import sys

def main():
    # Output must be strictly under 160 characters
    message = "All servers are currently on strike. Management is negotiating with the pixels. Expected resolution: never."
    
    # Ensure it's under the limit
    if len(message) > 160:
        print("Error: Message exceeds 160 characters", file=sys.stderr)
        sys.exit(1)
        
    print(message)

if __name__ == "__main__":
    main()