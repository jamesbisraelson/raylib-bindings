#include <filesystem>
#include "pocketpy.h"
using namespace pkpy;

namespace pkpy{
    void add_module_raylib(VM* vm);
}

int main(int argc, char** argv) {
    VM* vm = new VM();
    add_module_raylib(vm);

    std::string filepath;
    if (argc > 1) {
        filepath = argv[1];
    } else {
        filepath = "main.py";
    }

    int out_size;
    unsigned char* b = vm->_import_handler(filepath.c_str(), &out_size);
    if(!b){
        std::cerr << "Error: " << filepath << " not found" << std::endl;
        return 1;
    }
    vm->exec(std::string_view((char*)b, out_size)); 

    delete vm;
    return 0;
}