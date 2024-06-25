#include "pocketpy.h"
using namespace pkpy;

namespace pkpy{
    void add_module_raylib(VM* vm);
}

int main(){
    VM* vm = new VM();
    add_module_raylib(vm);

    std::string filepath = "main.py";
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