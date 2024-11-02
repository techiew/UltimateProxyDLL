#include <Windows.h>
#include <iostream>

#include "UltimateProxyDLL.h"

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
	if (fdwReason == DLL_PROCESS_ATTACH)
	{
		DisableThreadLibraryCalls(hinstDLL);
		try
		{	
			UPD::OpenDebugTerminal();
			UPD::CreateProxy(hinstDLL);
		}
		catch (std::runtime_error e)
		{
			std::cout << e.what() << std::endl;
			return FALSE;
		}
	}
	return TRUE;
}