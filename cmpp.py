#!/usr/bin/env python

import os

def create_cmakelists(project_name):
    with open("CMakeLists.txt", "w") as file:
        file.write(cmake_content)
    
    print(f"CMakeLists.txt for project '{project_name}' has been created.")

def create_main_file(project_name):
    os.makedirs("src", exist_ok=True)
    with open("src/main.cpp", "w") as file:
        file.write(main_content)


project_name = input("Enter your project name: ")

cmake_content = f"""cmake_minimum_required(VERSION 3.25)

project({project_name} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(
    {project_name}
    src/main.cpp
)
"""

main_content = f'''#include <iostream>


int main(const int argc, const char* argv[]) {{
    std::cout << "Hello from {project_name}!" << std::endl;

    return EXIT_SUCCESS;
}}
'''

create_cmakelists(project_name)
create_main_file(project_name)