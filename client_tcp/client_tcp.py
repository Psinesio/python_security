import socket
import sys  # pylint: disable=invalid-name


def main():
    try:
        # Create a TCP/IP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print(f"Error creating socket: {e}")
        sys.exit()

    print("Socket created successfully")

    hostAlvo = input("Enter the target host (IP address): ")
    portaAlvo = int(input("Enter the target port (number): "))

    try:
        # Connect the socket to the server
        s.connect((hostAlvo, portaAlvo))
        print(f"Connected to {hostAlvo} on port {portaAlvo}")
        s.shutdown(2)

    except socket.error as e:
        print(f"Error connecting to {hostAlvo} on port {portaAlvo}: {e}")
        sys.exit()


if __name__ == "__main__":
    main()
