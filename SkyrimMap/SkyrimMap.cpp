// SkyrimMap.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "Windows.h"
#include <conio.h>
#include <string>

#define MAPFILES "D:\\Steam\\steamapps\\common\\skyrim\\Data\\textures\\Maps\\Skyrim\\"
#define XOFFSET 57
#define YOFFSET 57


void RenameTGA (void)
{
	WIN32_FIND_DATA FindData;
	HANDLE hFind = FindFirstFileA(MAPFILES "tga\\*.tga", &FindData);
	if (hFind == INVALID_HANDLE_VALUE) return;
	BOOL Result;

	do
	{
		int Length = strlen(FindData.cFileName);

		if (Length > 6 && stricmp(FindData.cFileName + Length - 6, "00.tga") == 0 && Length < 200)
		{
			char Filename[256];
			strncpy(Filename, FindData.cFileName, 200);
			Filename[Length - 6] = 0;

			if (strnicmp(Filename, "Tamriel.", 8) == 0)
			{
				const char* pParse = Filename + 8;
				int X = atoi(pParse);
				
				while (*pParse != 0)
				{
					++pParse;

					if (*pParse == '.')
					{
						++pParse;
						break;
					}
				}

				int Y = atoi(pParse);

				
				std::string File1(MAPFILES);
				std::string File2(MAPFILES);
				File1 += "tga\\";
				File1 += FindData.cFileName;

				char Buffer[256];
				_snprintf(Buffer, 200, "skyrim_%03d_%03d.tga", X+XOFFSET, Y+YOFFSET);

				File2 += "tga\\";
				File2 += Buffer;

				printf ("Renaming '%s' to '%s'...\n", File1.c_str(), File2.c_str());
				MoveFileA(File1.c_str(), File2.c_str());
			}

		}
		
		Result = FindNextFileA(hFind, &FindData);
	} while (Result);

}

int _tmain(int argc, _TCHAR* argv[])
{
	RenameTGA();	
	_getch();
	return 0;
}

