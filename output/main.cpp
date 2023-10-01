#include "pocketpy.h"

using namespace pkpy;

namespace pkpy{
    void add_module_raylib(VM* vm);
}

int main(){
    VM* vm = new VM();
    add_module_raylib(vm);
    const char* filepath = "../main.py";
    Bytes b = vm->_import_handler(filepath);
    if(!b){
        std::cerr << "Error: " << filepath << " not found" << std::endl;
        return 1;
    }
    vm->exec(b.str());

    delete vm;
    return 0;
}