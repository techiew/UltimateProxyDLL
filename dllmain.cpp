#include <Windows.h>

#include "UniversalProxyDLL.h"

typedef HRESULT(*FpDirectInput8Create)(HINSTANCE, DWORD, REFIID, LPVOID*, LPUNKNOWN);
void* fpDirectInput8Create = nullptr;
HRESULT CallbackDirectInput8Create(HINSTANCE hinst, DWORD dwVersion, REFIID riidltf, LPVOID* ppvOut, LPUNKNOWN punkOuter)
{
	printf("Callback called!\n");
	return (*(FpDirectInput8Create*)fpDirectInput8Create)(hinst, dwVersion, riidltf, ppvOut, punkOuter);
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
	if (fdwReason == DLL_PROCESS_ATTACH)
	{
		UPD::OpenDebugTerminal();
		fpDirectInput8Create = UPD::RegisterCallback("DirectInput8Create", &CallbackDirectInput8Create);
		UPD::CreateProxy(hinstDLL);
	}
    return TRUE;
}
