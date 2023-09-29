#include "pocketpy.h"

using namespace pkpy;

namespace pkpy{
    void add_module_raylib(VM* vm);
}

int main(){
    VM* vm = new VM();
    add_module_raylib(vm);

    const char* filepath = "main.py";
    Str source = vm->_import_handler(filepath).str();
    vm->exec(source);

    delete vm;
    return 0;
}