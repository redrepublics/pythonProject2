Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "conv_avi_to_mp4.exe" & Chr(34), 0
Set WshShell = Nothing