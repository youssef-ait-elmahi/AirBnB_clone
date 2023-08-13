# 0x00. AirBnB Clone - The Console

This repository contains the code for an AirBnB clone console. The console is a command-line interface (CLI) application that allows users to interact with the AirBnB clone project. Users can manage objects like User, Place, State, City, Amenity, and Review, create, update, delete, and retrieve data, and perform various operations using commands.

## Installation

1. Clone this repository to your local machine.
   ```
   git clone https://github.com/youssef-ait-elmahi/AirBnB_clone.git
   ```

2. Navigate to the cloned directory.
   ```
   cd AirBnB_clone
   ```

3. Run the console.
   ```
   ./console.py
   ```

## Usage

Once the console is running, you can start interacting with it by entering commands. The basic structure of a command is:
```
(command name) (class name) (command arguments)
```

### Available Commands

- `create`: Creates a new instance of a class.
   Example: `create User`

- `show`: Displays information about a specific instance.
   Example: `show User 123`

- `destroy`: Deletes an instance.
   Example: `destroy User 123`

- `all`: Displays information about all instances of a class.
   Example: `all User`

- `update`: Updates attributes of an instance.
   Example: `update User 123 first_name "John"`

- `quit`: Exits the console.

## Examples

1. Create a new User instance:
   ```
   (hbnb) create User
   ```

2. Display information about a User instance:
   ```
   (hbnb) show User 123
   ```

3. Delete a User instance:
   ```
   (hbnb) destroy User 123
   ```

4. Display information about all User instances:
   ```
   (hbnb) all User
   ```

5. Update attributes of a User instance:
   ```
   (hbnb) update User 123 first_name "John"
   ```

## Author

This AirBnB clone console was developed by [youssef-ait-elmahi](youssefaitelmahi@gmail.com), [Ahmedkel](ahmedkeloch@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

We'd like to thank the original AirBnB team for inspiring this project. Special thanks to the mentors and fellow learners who contributed to the development of this console.
