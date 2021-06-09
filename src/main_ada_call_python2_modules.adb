
-- IMPORT STANDARD ADA PACKAGES
with Ada.Text_IO;   -- use  Ada.Text_IO;
with Ada.Real_Time; -- use  Ada.Real_Time;
-- with Interfaces;

-- IMPORT USER-DEFINED ADA PACKAGES 
-- (LOOKS FOR CORRESPONDING NAMED .ads FILE)
with pkg_ada_datetime_stamp;
with pkg_ada_realtime_delays;
with pkg_ada_callpython_module;

-- ========================================================
procedure main_ada_call_python2_modules 
-- ========================================================
is   
   -- IMPORT STANDARD ADA PACKAGES
-- RENAME STANDARD ADA PACKAGES FOR CONVENIENCE
   package ATIO   renames Ada.Text_IO;
   package ART    renames Ada.Real_Time;
      
   -- RENAME USER-DEFINED ADA PACKAGES FOR CONVENIENCE
   package PADTS  renames pkg_ada_datetime_stamp;
   package PARD   renames pkg_ada_realtime_delays;
   package PACPM  renames pkg_ada_callpython_module;
   
   -- VARIABLE DECLARATIONS
   startClock, finishClock   : ART.Time;  
      
   ModuleDir       : String := "src/python-modules/"; 
   ModuleName_main : String := "python_main";
   ModuleName_01   : String := "python_module_01";  -- No need .py suffix
   ModuleName_02   : String := "python_module_02";  -- No need .py suffix
     
   Module_main : PACPM.Module;  -- DEFINE TYPE
   Module_01   : PACPM.Module;  -- DEFINE TYPE
   -- Module_02   : PACPM.Module;
   
   A : Integer := 10;
   B : Integer := 2;
   Result : Integer;
   
-- ========================================================   
begin  -- FOR procedure MAIN
   startClock := ART.Clock; PADTS.dtstamp;
   ATIO.Put_Line ("STARTED: main Bismillah 3 times WRY");
   ATIO.New_Line;
   
   -- CODE BEGINS HERE
   PACPM.Initialize;

   -- =====================================================
   PADTS.dtstamp;
   ATIO.Put_Line ("TEST 1 - Ada executing Python commands directly (in Ada environment)");
   PADTS.dtstamp;
   ATIO.Put_Line ("Executing... PACPM.Execute_String (""import numpy as np"") ");
   PACPM.Execute_String ("import numpy as np");
   PADTS.dtstamp;
   ATIO.Put_Line ("Executing... PACPM.Execute_String (""x = np.arange(0.0, 10.0, 0.1)"") ");
   PACPM.Execute_String ("x = np.arange(0.0, 10.0, 0.1)");
   ATIO.New_Line;
      
   -- =====================================================
   PADTS.dtstamp;
   ATIO.Put_Line ("TEST 2 - Loading external computational Python module and calling itd functions (parameters):");
   PADTS.dtstamp;
   ATIO.Put_Line ("Loading module from file  : " & ModuleDir & ModuleName_01 & ".py");
   Module_01 := PACPM.Import_File (ModuleName_01);  
   ATIO.New_Line;
   
   PADTS.dtstamp;
   ATIO.Put_Line ("Call python to add two integers - send 2 parameters:");
   Result := PACPM.Call (Module_01, "add", A, B);
   PADTS.dtstamp;
   ATIO.Put_Line ("Ada received return from Python add, Result = " & Integer'Image (Result));
   ATIO.New_Line;
   
   PADTS.dtstamp;
   ATIO.Put_Line ("Call python to divide two integers - send 2 parameters:");
   Result := PACPM.Call (Module_01, "divide", A, B);
   PADTS.dtstamp;
   ATIO.Put_Line ("Ada received return from Python divide, Result = " & Integer'Image (Result));
   ATIO.New_Line;
  
   -- =====================================================   
   PADTS.dtstamp;
   ATIO.Put_Line ("TEST 3 - Loading external Python module and calling functions from that module:");
   PADTS.dtstamp;
   ATIO.Put_Line ("Loading module from file  : " & ModuleDir & ModuleName_main & ".py");
   
   Module_main := PACPM.Import_File (ModuleName_main);  -- LOADING PYTHON2.7 MODULE
   ATIO.New_Line;
   PACPM.Call (Module_main, "opening_main");  -- Calling procedure opening_main() in module : python_main.py
   PACPM.Call (Module_main, "execute_main");  -- Calling procedure execute_main() in module : python_main.py
   PACPM.Call (Module_main, "pythonversion_main");     
   PACPM.Call (Module_main, "closing_main");  
   ATIO.New_Line;
   
   
   PACPM.Close_Module (Module_01);
   PACPM.Close_Module (Module_main);
   PACPM.Finalize;
   -- =====================================================
   -- ONLY FIVE(5) STEPS IN ADA TO CALL PYTHON MODULES
   -- =====================================================
   -- PACPM.Initialize;
   -- Module_02 := PACPM.Import_File (ModuleName_02);   -- The python file without .py
   -- PACPM.Call (Module_02, "hello");
   -- PACPM.Close_Module (Module_02);
   -- PACPM.Finalize;
      
   -- CODE ENDS HERE
   -- =====================================================
   ATIO.New_Line; PADTS.dtstamp;
   ATIO.Put ("ENDED: main Alhamdulillah 3 times WRY. ");
   finishClock := ART.Clock;
   PARD.exec_display_execution_time(startClock, finishClock); 
   
-- ========================================================   
end main_ada_call_python2_modules;
-- ========================================================

