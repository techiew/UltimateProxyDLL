#include <Windows.h>
#include <iostream>

#include "UltimateProxyDLL.h"

DWORD WINAPI NewThread(LPVOID lpParam)
{
	printf("Doing some very naughty stuff\n");
	return 0;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
	if (fdwReason == DLL_PROCESS_ATTACH)
	{
		try
		{	
			upd::enable_logging();
			upd::open_debug_terminal();
			upd::create_proxy_and_thread(hinstDLL, &NewThread);
		}
		catch (std::runtime_error e)
		{
			std::cout << e.what() << std::endl;
			return FALSE;
		}
	}
	return TRUE;
}