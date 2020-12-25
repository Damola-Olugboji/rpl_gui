function varargout = viscosity_gui_gen_complete(varargin)
% VISCOSITY_GUI_GEN_COMPLETE MATLAB code for viscosity_gui_gen_complete.fig
%      VISCOSITY_GUI_GEN_COMPLETE, by itself, creates a new VISCOSITY_GUI_GEN_COMPLETE or raises the existing
%      singleton*.
%
%      H = VISCOSITY_GUI_GEN_COMPLETE returns the handle to a new VISCOSITY_GUI_GEN_COMPLETE or the handle to
%      the existing singleton*.
%
%      VISCOSITY_GUI_GEN_COMPLETE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in VISCOSITY_GUI_GEN_COMPLETE.M with the given input arguments.
%
%      VISCOSITY_GUI_GEN_COMPLETE('Property','Value',...) creates a new VISCOSITY_GUI_GEN_COMPLETE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before viscosity_gui_gen_complete_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to viscosity_gui_gen_complete_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help viscosity_gui_gen_complete

% Last Modified by GUIDE v2.5 01-Nov-2020 20:56:14

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @viscosity_gui_gen_complete_OpeningFcn, ...
                   'gui_OutputFcn',  @viscosity_gui_gen_complete_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before viscosity_gui_gen_complete is made visible.
function viscosity_gui_gen_complete_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to viscosity_gui_gen_complete (see VARARGIN)

% Choose default command line output for viscosity_gui_gen_complete
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes viscosity_gui_gen_complete wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = viscosity_gui_gen_complete_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mw1_Callback(hObject, eventdata, handles)
% hObject    handle to mw1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mw1 as text
%        str2double(get(hObject,'String')) returns contents of mw1 as a double
mw1_a = get(handles.mw1,'String');
mw1_a = str2num(mw1_a);
setappdata(0,'mw_1',mw1_a);


% --- Executes during object creation, after setting all properties.
function mw1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mw1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mw2_Callback(hObject, eventdata, handles)
% hObject    handle to mw2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mw2 as text
%        str2double(get(hObject,'String')) returns contents of mw2 as a double
mw2_a = get(handles.mw2,'String');
mw2_a = str2num(mw2_a);
setappdata(0,'mw_2',mw2_a);

% --- Executes during object creation, after setting all properties.
function mw2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mw2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mw3_Callback(hObject, eventdata, handles)
% hObject    handle to mw3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mw3 as text
%        str2double(get(hObject,'String')) returns contents of mw3 as a double
mw3_a = get(handles.mw3,'String');
mw3_a = str2num(mw3_a);
setappdata(0,'mw_3',mw3_a);

% --- Executes during object creation, after setting all properties.
function mw3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mw3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mw4_Callback(hObject, eventdata, handles)
% hObject    handle to mw4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mw4 as text
%        str2double(get(hObject,'String')) returns contents of mw4 as a double
mw4_a = get(handles.mw4,'String');
mw4_a = str2num(mw4_a);
setappdata(0,'mw_4',mw4_a);

% --- Executes during object creation, after setting all properties.
function mw4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mw4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mw5_Callback(hObject, eventdata, handles)
% hObject    handle to mw5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mw5 as text
%        str2double(get(hObject,'String')) returns contents of mw5 as a double
mw5_a = get(handles.mw5,'String');
mw5_a = str2num(mw5_a);
setappdata(0,'mw_5',mw5_a);

% --- Executes during object creation, after setting all properties.
function mw5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mw5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mf1_Callback(hObject, eventdata, handles)
% hObject    handle to mf1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mf1 as text
%        str2double(get(hObject,'String')) returns contents of mf1 as a double
mf1_a = get(handles.mf1,'String');
mf1_a = str2num(mf1_a);
setappdata(0,'mf_1',mf1_a);

% --- Executes during object creation, after setting all properties.
function mf1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mf1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mf2_Callback(hObject, eventdata, handles)
% hObject    handle to mf2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mf2 as text
%        str2double(get(hObject,'String')) returns contents of mf2 as a double
mf2_a = get(handles.mf2,'String');
mf2_a = str2num(mf2_a);
setappdata(0,'mf_2',mf2_a);

% --- Executes during object creation, after setting all properties.
function mf2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mf2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mf3_Callback(hObject, eventdata, handles)
% hObject    handle to mf3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mf3 as text
%        str2double(get(hObject,'String')) returns contents of mf3 as a double
mf3_a = get(handles.mf3,'String');
mf3_a = str2num(mf3_a);
setappdata(0,'mf_3',mf3_a);

% --- Executes during object creation, after setting all properties.
function mf3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mf3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mf4_Callback(hObject, eventdata, handles)
% hObject    handle to mf4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mf4 as text
%        str2double(get(hObject,'String')) returns contents of mf4 as a double
mf4_a = get(handles.mf4,'String');
mf4_a = str2num(mf4_a);
setappdata(0,'mf_4',mf4_a);

% --- Executes during object creation, after setting all properties.
function mf4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mf4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function mf5_Callback(hObject, eventdata, handles)
% hObject    handle to mf5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of mf5 as text
%        str2double(get(hObject,'String')) returns contents of mf5 as a double
mf5_a = get(handles.mf5,'String');
mf5_a = str2num(mf5_a);
setappdata(0,'mf_5',mf5_a);

% --- Executes during object creation, after setting all properties.
function mf5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to mf5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function bp1_Callback(hObject, eventdata, handles)
% hObject    handle to bp1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of bp1 as text
%        str2double(get(hObject,'String')) returns contents of bp1 as a double
bp1_a = get(handles.bp1,'String');
bp1_a = str2num(bp1_a);
setappdata(0,'bp_1',bp1_a);

% --- Executes during object creation, after setting all properties.
function bp1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to bp1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function bp2_Callback(hObject, eventdata, handles)
% hObject    handle to bp2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of bp2 as text
%        str2double(get(hObject,'String')) returns contents of bp2 as a double
bp2_a = get(handles.bp2,'String');
bp2_a = str2num(bp2_a);
setappdata(0,'bp_2',bp2_a);

% --- Executes during object creation, after setting all properties.
function bp2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to bp2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function bp3_Callback(hObject, eventdata, handles)
% hObject    handle to bp3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of bp3 as text
%        str2double(get(hObject,'String')) returns contents of bp3 as a double
bp3_a = get(handles.bp3,'String');
bp3_a = str2num(bp3_a);
setappdata(0,'bp_3',bp3_a);

% --- Executes during object creation, after setting all properties.
function bp3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to bp3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function bp4_Callback(hObject, eventdata, handles)
% hObject    handle to bp4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of bp4 as text
%        str2double(get(hObject,'String')) returns contents of bp4 as a double
bp4_a = get(handles.bp4,'String');
bp4_a = str2num(bp4_a);
setappdata(0,'bp_4',bp4_a);

% --- Executes during object creation, after setting all properties.
function bp4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to bp4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function bp5_Callback(hObject, eventdata, handles)
% hObject    handle to bp5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of bp5 as text
%        str2double(get(hObject,'String')) returns contents of bp5 as a double
bp5_a = get(handles.bp5,'String');
bp5_a = str2num(bp5_a);
setappdata(0,'bp_5',bp5_a);

% --- Executes during object creation, after setting all properties.
function bp5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to bp5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function db1_Callback(hObject, eventdata, handles)
% hObject    handle to db1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of db1 as text
%        str2double(get(hObject,'String')) returns contents of db1 as a double
db1_a = get(handles.db1,'String');
db1_a = str2num(db1_a);
setappdata(0,'db_1',db1_a);

% --- Executes during object creation, after setting all properties.
function db1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to db1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function db2_Callback(hObject, eventdata, handles)
% hObject    handle to db2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of db2 as text
%        str2double(get(hObject,'String')) returns contents of db2 as a double
db2_a = get(handles.db2,'String');
db2_a = str2num(db2_a);
setappdata(0,'db_2',db2_a);

% --- Executes during object creation, after setting all properties.
function db2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to db2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function db3_Callback(hObject, eventdata, handles)
% hObject    handle to db3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of db3 as text
%        str2double(get(hObject,'String')) returns contents of db3 as a double
db3_a = get(handles.db3,'String');
db3_a = str2num(db3_a);
setappdata(0,'db_3',db3_a);

% --- Executes during object creation, after setting all properties.
function db3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to db3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function db4_Callback(hObject, eventdata, handles)
% hObject    handle to db4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of db4 as text
%        str2double(get(hObject,'String')) returns contents of db4 as a double
db4_a = get(handles.db4,'String');
db4_a = str2num(db4_a);
setappdata(0,'db_4',db4_a);

% --- Executes during object creation, after setting all properties.
function db4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to db4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function db5_Callback(hObject, eventdata, handles)
% hObject    handle to db5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of db5 as text
%        str2double(get(hObject,'String')) returns contents of db5 as a double
db5_a = get(handles.db5,'String');
db5_a = str2num(db5_a);
setappdata(0,'db_5',db5_a);

% --- Executes during object creation, after setting all properties.
function db5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to db5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function dm1_Callback(hObject, eventdata, handles)
% hObject    handle to dm1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of dm1 as text
%        str2double(get(hObject,'String')) returns contents of dm1 as a double
dm1_a = get(handles.dm1,'String');
dm1_a = str2num(dm1_a);
setappdata(0,'dm_1',dm1_a);

% --- Executes during object creation, after setting all properties.
function dm1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to dm1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function dm2_Callback(hObject, eventdata, handles)
% hObject    handle to dm2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of dm2 as text
%        str2double(get(hObject,'String')) returns contents of dm2 as a double
dm2_a = get(handles.dm2,'String');
dm2_a = str2num(dm2_a);
setappdata(0,'dm_2',dm2_a);

% --- Executes during object creation, after setting all properties.
function dm2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to dm2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function dm3_Callback(hObject, eventdata, handles)
% hObject    handle to dm3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of dm3 as text
%        str2double(get(hObject,'String')) returns contents of dm3 as a double
dm3_a = get(handles.dm3,'String');
dm3_a = str2num(dm3_a);
setappdata(0,'dm_3',dm3_a);

% --- Executes during object creation, after setting all properties.
function dm3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to dm3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function dm4_Callback(hObject, eventdata, handles)
% hObject    handle to dm4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of dm4 as text
%        str2double(get(hObject,'String')) returns contents of dm4 as a double
dm4_a = get(handles.dm4,'String');
dm4_a = str2num(dm4_a);
setappdata(0,'dm_4',dm4_a);

% --- Executes during object creation, after setting all properties.
function dm4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to dm4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function dm5_Callback(hObject, eventdata, handles)
% hObject    handle to dm5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of dm5 as text
%        str2double(get(hObject,'String')) returns contents of dm5 as a double
dm5_a = get(handles.dm5,'String');
dm5_a = str2num(dm5_a);
setappdata(0,'dm_5',dm5_a);

% --- Executes during object creation, after setting all properties.
function dm5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to dm5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%THIS IS EXTRANEOUS CODE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes on selection change in chem1_popup.
function chem1_popup_Callback(hObject, eventdata, handles)
% hObject    handle to chem1_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns chem1_popup contents as cell array
%        contents{get(hObject,'Value')} returns selected item from chem1_popup

contents = cellstr(get(handles.chem1_popup,'String'));
popup_choice = contents{get(handles.chem1_popup,'Value')};

if (strcmp(popup_choice,'Nitrogen (N2)'))
    func_option = 1; 
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Hydrogen (H2)'))
    func_option = 2;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Monoxide (CO)'))
    func_option = 3;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Dioxide (CO2)'))
    func_option = 4;
    setappdata(0,'chem1_popup',func_option);

elseif (strcmp(popup_choice,'Hydrochloride (HCL)'))
    func_option = 5;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Oxygen (O2)'))
    func_option = 6;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Helium (He)'))
    func_option = 7;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Neon (Ne)'))
    func_option = 8;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Xenon (Xe)'))
    func_option = 9;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'Krypton (Kr)'))
    func_option = 10;
    setappdata(0,'chem1_popup',func_option);
    
elseif (strcmp(popup_choice,'None'))
    func_option = 0; 
    setappdata(0,'chem1_popup',func_option);

end

% --- Executes during object creation, after setting all properties.
function chem1_popup_CreateFcn(hObject, eventdata, handles)
% hObject    handle to chem1_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes on selection change in chem2_popup.
function chem2_popup_Callback(hObject, eventdata, handles)
% hObject    handle to chem2_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns chem2_popup contents as cell array
%        contents{get(hObject,'Value')} returns selected item from chem2_popup

contents = cellstr(get(handles.chem2_popup,'String'));
popup_choice = contents{get(handles.chem2_popup,'Value')};

if (strcmp(popup_choice,'Nitrogen (N2)'))
    func_option = 1; 
    setappdata(0,'chem2_popup',func_option);

elseif (strcmp(popup_choice,'Hydrogen (H2)'))
    func_option = 2;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Monoxide (CO)'))
    func_option = 3;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Dioxide (CO2)'))
    func_option = 4;
    setappdata(0,'chem2_popup',func_option);

elseif (strcmp(popup_choice,'Hydrochloride (HCL)'))
    func_option = 5;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Oxygen (O2)'))
    func_option = 6;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Helium (He)'))
    func_option = 7;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Neon (Ne)'))
    func_option = 8;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Xenon (Xe)'))
    func_option = 9;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Krypton (Kr)'))
    func_option = 10;
    setappdata(0,'chem2_popup',func_option);

elseif (strcmp(popup_choice,'None'))
    func_option = 0; 
    setappdata(0,'chem2_popup',func_option);
    
end

% --- Executes during object creation, after setting all properties.
function chem2_popup_CreateFcn(hObject, eventdata, handles)
% hObject    handle to chem2_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes on selection change in chem3_popup.
function chem3_popup_Callback(hObject, eventdata, handles)
% hObject    handle to chem3_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns chem3_popup contents as cell array
%        contents{get(hObject,'Value')} returns selected item from chem3_popup

contents = cellstr(get(handles.chem3_popup,'String'));
popup_choice = contents{get(handles.chem3_popup,'Value')};

if (strcmp(popup_choice,'Nitrogen (N2)'))
    func_option = 1; 
    setappdata(0,'chem3_popup',func_option);

elseif (strcmp(popup_choice,'Hydrogen (H2)'))
    func_option = 2;
    setappdata(0,'chem3_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Monoxide (CO)'))
    func_option = 3;
    setappdata(0,'chem3_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Dioxide (CO2)'))
    func_option = 4;
    setappdata(0,'chem3_popup',func_option);

elseif (strcmp(popup_choice,'Hydrochloride (HCL)'))
    func_option = 5;
    setappdata(0,'chem3_popup',func_option);
    
elseif (strcmp(popup_choice,'Oxygen (O2)'))
    func_option = 6;
    setappdata(0,'chem3_popup',func_option);
    
elseif (strcmp(popup_choice,'Helium (He)'))
    func_option = 7;
    setappdata(0,'chem2_popup',func_option);
    
elseif (strcmp(popup_choice,'Neon (Ne)'))
    func_option = 8;
    setappdata(0,'chem3_popup',func_option);
    
elseif (strcmp(popup_choice,'Xenon (Xe)'))
    func_option = 9;
    setappdata(0,'chem3_popup',func_option);
    
elseif (strcmp(popup_choice,'Krypton (Kr)'))
    func_option = 10;
    setappdata(0,'chem3_popup',func_option);

elseif (strcmp(popup_choice,'None'))
    func_option = 0; 
    setappdata(0,'chem3_popup',func_option);
    
end

% --- Executes during object creation, after setting all properties.
function chem3_popup_CreateFcn(hObject, eventdata, handles)
% hObject    handle to chem3_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes on selection change in chem4_popup.
function chem4_popup_Callback(hObject, eventdata, handles)
% hObject    handle to chem4_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns chem4_popup contents as cell array
%        contents{get(hObject,'Value')} returns selected item from chem4_popup

contents = cellstr(get(handles.chem4_popup,'String'));
popup_choice = contents{get(handles.chem4_popup,'Value')};

if (strcmp(popup_choice,'Nitrogen (N2)'))
    func_option = 1; 
    setappdata(0,'chem4_popup',func_option);

elseif (strcmp(popup_choice,'Hydrogen (H2)'))
    func_option = 2;
    setappdata(0,'chem4_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Monoxide (CO)'))
    func_option = 3;
    setappdata(0,'chem4_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Dioxide (CO2)'))
    func_option = 4;
    setappdata(0,'chem4_popup',func_option);

elseif (strcmp(popup_choice,'Hydrochloride (HCL)'))
    func_option = 5;
    setappdata(0,'chem4_popup',func_option);
    
elseif (strcmp(popup_choice,'Oxygen (O2)'))
    func_option = 6;
    setappdata(0,'chem4_popup',func_option);
    
elseif (strcmp(popup_choice,'Helium (He)'))
    func_option = 7;
    setappdata(0,'chem4_popup',func_option);
    
elseif (strcmp(popup_choice,'Neon (Ne)'))
    func_option = 8;
    setappdata(0,'chem4_popup',func_option);
    
elseif (strcmp(popup_choice,'Xenon (Xe)'))
    func_option = 9;
    setappdata(0,'chem4_popup',func_option);
    
elseif (strcmp(popup_choice,'Krypton (Kr)'))
    func_option = 10;
    setappdata(0,'chem4_popup',func_option);    

elseif (strcmp(popup_choice,'None'))
    func_option = 0; 
    setappdata(0,'chem4_popup',func_option);
    
end

% --- Executes during object creation, after setting all properties.
function chem4_popup_CreateFcn(hObject, eventdata, handles)
% hObject    handle to chem4_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes on selection change in chem5_popup.
function chem5_popup_Callback(hObject, eventdata, handles)
% hObject    handle to chem5_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns chem5_popup contents as cell array
%        contents{get(hObject,'Value')} returns selected item from chem5_popup


contents = cellstr(get(handles.chem5_popup,'String'));
popup_choice = contents{get(handles.chem5_popup,'Value')};

if (strcmp(popup_choice,'Nitrogen (N2)'))
    func_option = 1; 
    setappdata(0,'chem5_popup',func_option);

elseif (strcmp(popup_choice,'Hydrogen (H2)'))
    func_option = 2;
    setappdata(0,'chem5_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Monoxide (CO)'))
    func_option = 3;
    setappdata(0,'chem5_popup',func_option);
    
elseif (strcmp(popup_choice,'Carbon Dioxide (CO2)'))
    func_option = 4;
    setappdata(0,'chem5_popup',func_option);

elseif (strcmp(popup_choice,'Hydrochloride (HCL)'))
    func_option = 5;
    setappdata(0,'chem5_popup',func_option);
    
elseif (strcmp(popup_choice,'Oxygen (O2)'))
    func_option = 6;
    setappdata(0,'chem5_popup',func_option);
    
elseif (strcmp(popup_choice,'Helium (He)'))
    func_option = 7;
    setappdata(0,'chem5_popup',func_option);
    
elseif (strcmp(popup_choice,'Neon (Ne)'))
    func_option = 8;
    setappdata(0,'chem5_popup',func_option);
    
elseif (strcmp(popup_choice,'Xenon (Xe)'))
    func_option = 9;
    setappdata(0,'chem5_popup',func_option);
    
elseif (strcmp(popup_choice,'Krypton (Kr)'))
    func_option = 10;
    setappdata(0,'chem5_popup',func_option);

elseif (strcmp(popup_choice,'None'))
    func_option = 0; 
    setappdata(0,'chem5_popup',func_option);
    
end

% --- Executes during object creation, after setting all properties.
function chem5_popup_CreateFcn(hObject, eventdata, handles)
% hObject    handle to chem5_popup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

%% INPUT

popup_choice = zeros(1,5);

for w = 1:length(popup_choice)
    
    phr = sprintf('chem%1.0f_popup',w);
    popup_choice(w) = getappdata(0,phr); % popup_choice is obtaining the values of func_option which determines what chemical was picked
end

num = 0;

if popup_choice(1) ~= 0
    num=num+1;
    if popup_choice(2) ~= 0
        num=num+1;
        if popup_choice(3) ~= 0
            num=num+1;
            if popup_choice(4) ~=0
                num=num+1;
                if popup_choice(5) ~= 0
                    num=num+1;
                end
            end
        end
    end
end

fprintf("Detected %1.0f chemicals.\n",num);

temp = 1; %[k]; initial value of the reference temperature value, will eventually reach 3500k. 
visc_gas_mix_a = zeros(1,3500); % array that will contain all values of the viscosity gas mixture at each reference temp value.

for aaa = 1:3500 % 3490 iterations for each temp value
        
    mu_a = zeros(1,num); % viscosity constituent array (calc'ed)
    therm_a = zeros(1,num); % therm. cond. constituent array (calc'ed)
    
    mw_a = zeros(1,num); % molecular wt. array (inputted)
    mf_a = zeros(1,num); % molar fraction array (inputted)
    
    sigma_a  = zeros(1,num); % sigma array (tabulated)
    ek_a = zeros(1,num); % e/k array (tabulated)
    
    bp_a = zeros(1,num); % boiling point array (inputted)
    db_a = zeros(1,num); % density at boilng point array (inputted)
    dm_a = zeros(1,num); % dipole moment array (inputted)
    mv_a = zeros(1,num); % boiling point molar volume array (calc'ed)
        
    %retrieving user input array
    for w=1:num
        
        % All equations below have been referenced by Appendix C
                
        if popup_choice(w) == 1 % calculate nitrogen (N2) 

            mu_a(w) = (42.606 +(4.75*10^-1)*temp +((-9.88*10^-5)*temp^2))*(10^-2); %viscosity (good for 150-1500k) - [10^-5 Pa*s]
            therm_a(w) = 0.00309 +(7.5930*10^-5)*temp+((-1.1014*10^-8)*temp^2); %therm c (good for 78-1500k) - (W/m*k)
            sigma_a(w) = 3.798;
            ek_a(w) = 71.4;

        elseif popup_choice(w) == 2 % calculate hydrogen (H2) 

            mu_a(w) = (27.758 +(2.12*10^-1)*temp +((-3.28*10^-5)*temp^2))*(10^-2); %viscosity (good for 150-1500k) - [10^-5 Pa*s]
            therm_a(w) = 0.03951 +(4.5918*10^-4)*temp +((-6.4933*10^-8)*temp^2); %therm c (good for 78-1500k) - (W/m*k)
            sigma_a(w) = 2.827;
            ek_a(w) = 59.7;

        elseif popup_choice(w) == 3 % calculate carbon monoxide (CO)

            mu_a(w) = (23.811 +(5.3944*10^-1)*temp +((-1.5411*10^-4)*temp^2))*(10^-2); %viscosity (good for 68-1250k) - [10^-5 Pa*s]
            therm_a(w) = 0.00158 +(8.2511*10^-5)*temp +((-1.9081*10^-8)*temp^2); %therm c (good for 70-1250k) - (W/m*k)
            sigma_a(w) = 3.690;
            ek_a(w) = 91.7;
            
        elseif popup_choice(w) == 4 % calculate carbon dioxide (CO2) 

            mu_a(w) = (11.811 +(4.983*10^-1)*temp +((-1.0851*10^-4)*temp^2))*(10^-2); %viscosity (good for 195-1500k) - [10^-5 Pa*s]
            therm_a(w) = -0.01200 +(1.0208*10^-4)*temp +((-2.2403*10^-8)*temp^2);
            sigma_a(w) = 3.941;
            ek_a(w) = 195.2;
            
        elseif popup_choice(w) == 5 % calculate hydrochloride (HCL) 

            mu_a(w) = (-9.118 +(5.55*10^-1)*temp +((-1.11*10^-4)*temp^2))*(10^-2); %viscosity (good for 200-1000k) - [10^-5 Pa*s]
            therm_a(w) = 0.00119 +(4.4775*10^-5)*temp +((2.0997*10^-10)*temp^2); %therm c (good for 159-1000k) - [10^-5 Pa*s]
            sigma_a(w) = 3.339;
            ek_a(w) = 344.7;
            
        elseif popup_choice(w) == 6 % calculate oxygen (O2) 

            mu_a(w) = (44.224 +(5.6200*10^-1)*temp +((-1.1300*10^-4)*temp^2))*(10^-2); %viscosity (good for 150-1500k) - [10^-5 Pa*s]
            therm_a(w) = 0.00121 +(8.6157*10^-5)*temp +((-1.3346*10^-8)*temp^2); %therm c (good for 80-1500k) - (W/m*k)
            sigma_a(w) = 3.467;
            ek_a(w) = 106.7;
            
        elseif popup_choice(w) == 7 % calculate helium (He)
        
            mu_a(w) = (7.29 +(0.03884)*temp +((-1.937*10^-6)*temp^2))*(10^-2); %viscosity (good for 20-5000k) - [10^-5 Pa*s from 10^-7 Pa*s]
            therm_a(w) = (47.25 +(0.3127)*temp +((-1.688*10^-5)*temp^2))*(10^-3); %therm c (good for 5-5000k) - (W/m*k) from (mW/m*k)
            sigma_a(w) = 2.608; %before used: 2.551 / 2.608
            ek_a(w) = 10.22;
            
        % Neon (8)
        
        elseif popup_choice(w) == 8 % calculate neon (Ne)
           
            mu_a(w) = (10.22 +(0.06096)*temp +((-4.265*10^-6)*temp^2))*(10^-2); %viscosity (good for 27.09-5000k) - [10^-5 Pa*s from 10^-7 Pa*s]
            therm_a(w) = (15.98 +(0.09441)*temp +((-6.604*10^-6)*temp^2))*(10^-3); %therm c (good for 27.09-5000k) - (W/m*k from mW/m*k)
            sigma_a(w) = 2.820; % 2.764
            ek_a(w) = 32.8; % 40.2

        % Xenon (9)
        
        elseif popup_choice(w) == 9 % calculate xenon (Xe)
            
           mu_a(w) = (7.755 +(0.05746)*temp +((-4.062*10^-6)*temp^2))*(10^-2); %viscosity (good for 165-5000k) - [10^-5 Pa*s from 10^-7 Pa*s]
           therm_a(w) = (1.887 +(0.01366)*temp +((-9.619*10^-7)*temp^2))*(10^-3); %therm c (good for 165-5000k) - (W/m*k from mW/m*k)
           sigma_a(w) = 4.082; 
           ek_a(w) = 206.9;
            
        % Krypton (10)
            
        elseif popup_choice(w) == 10 % calculate krypton (Kr)
            
           mu_a(w) = (9.019 +(0.05749)*temp +((-4.072*10^-6)*temp^2))*(10^-2); %viscosity (good for 120-5000k) - [10^-5 Pa*s from 10^-7 Pa*s]
           therm_a(w) = (3.404 +(0.02143)*temp +((-1.515*10^-6)*temp^2))*(10^-3); %therm c (good for 120-5000k) - (W/m*k from mW/m*k)
           sigma_a(w) = 3.610; % 3.690 or 3.610 
           ek_a(w) = 164.7; % 164.7 or 190 
            
        end
    end

    %retrieving user input of molecular wt. array [g/mol]

    for w=1:num
        phr = sprintf('mw_%1.0f',w);
        mw_a(w) = getappdata(0,phr);

    end

    %retrieving user input of molar fraction array [dimensionless]

    for w=1:num
        phr = sprintf('mf_%1.0f',w);
        mf_a(w) = getappdata(0,phr);

    end

    %retrieving user input of boiling point array [k]

    for w=1:num
        phr = sprintf('bp_%1.0f',w);
        bp_a(w) = getappdata(0,phr);

    end

    %retrieving user input of density at boiling point array [kg/m^3]

    for w=1:num
        phr = sprintf('db_%1.0f',w);
        db_a(w) = getappdata(0,phr);
    end

    %retrieving user input of dipole moment array [debyes/3.335*10^-30 C*m]

    for w=1:num
        phr = sprintf('dm_%1.0f',w);
        dm_a(w) = (3.335640*10^-30)*(getappdata(0,phr));

    end

    %calculating molar volume at boiling point [m^3/mol]
    for w=1:num

        mv_a(w) = mw_a(w)*(1/db_a(w))*(1/1000); % (1000*(g/mol)) / (kg/m^3)

    end

    %% ------- VISCOSITY GAS MIXTURE CALCULATION PART ---------
        
    %% A coefficient (and m coefficient) logic

    % Pre-located space for m coefficinet

    num_coef = num*num;

    m_coef  = zeros(1,num_coef);
    i = 1; % counter 
    j = 1; % 2nd counter

    for w=1:length(m_coef)

        m_coef(w) = ((4*mw_a(i)*mw_a(j))/(mw_a(i)+mw_a(j))^2)^0.25; % Referenced from page 4

        if j==num
            j = 1; % resetting j subscript
            i = i+1; % increasing i subscript
        else 
        j = j+1; % increasing j subscript
        end 
    end

    A_coef = zeros(1,num_coef);
    num_bracket = zeros(1,num_coef);
    denom_bracket = zeros(1,num_coef);
    bracket = zeros(1,num_coef);

    i = 1; % counter
    j = 1; % 2nd counter

    % A-coefficient logic

    for w=1:length(A_coef)

        num_bracket(w) = (mw_a(i)/mw_a(j))-(mw_a(i)/mw_a(j))^0.45;
        denom_bracket(w) = 2*(1+(mw_a(i)/mw_a(j)))+((1+((mw_a(i)/mw_a(j))^0.45))/(1+m_coef(w)))*m_coef(w);
        bracket(w)= (1+((num_bracket(w))/(denom_bracket(w))));

        A_coef(w) = m_coef(w)*((mw_a(j)/mw_a(i))^.5)*(bracket(w)); % Referenced from eq 9

        if j==num
            j = 1;
            i = i+1;
        else
            j=j+1;
        end
    end

    %% S coefficient logic

    delta = zeros(1,num); % For nonpolar gases, the polarity will equal to zero due to the dipole moment of the gas being zero. 
    for w=1:length(delta)

        delta(w) = (2*10^3)*(((dm_a(w))^2)/(bp_a(w)*mv_a(w)));

    end

    rduc_temp = zeros(1,num);
    for w=1:length(rduc_temp)

       rduc_temp(w) = temp/(1.15*bp_a(w)*(1+0.85*delta(w)^2));

    end

    % s-coefficient logic

    S_coef = zeros(1,num_coef);
    num_scoef = zeros(1,num_coef);
    denom_scoef = zeros(1,num_coef);

    i = 1; % counter
    j = 1; % 2nd counter

    for w=1:length(S_coef)

        num_scoef(w) = 1+((rduc_temp(i)*rduc_temp(j))^0.5)+((delta(i)*delta(j))/4);
        denom_scoef(w) = ((1+rduc_temp(i)+((delta(i)^2)/4))^0.5)*((1+rduc_temp(j)+((delta(j)^2)/4))^0.5);

        S_coef(w) = ((num_scoef(w))/(denom_scoef(w)));

        if j==num
            j = 1;
            i = i+1;
        else
            j=j+1;
        end

    end

    %% Viscosity Mixture logic

    i=1; %i-subscript counter
    j=1; %j-subscript counter

    if num == 2 

        denom_sum_comp = zeros(1,num_coef); % pre-locating space for S11 w/ A11, S12 w/ A12, S21 w/ A21, S22 w/ A22 denaminators, before they become i=1 and i=2 denaminators 

        for w=1:length(denom_sum_comp)

            denom_sum_comp(w) = (S_coef(i)*A_coef(i))*(mf_a(j)/sqrt(mu_a(j)));
            %disp(j);

            if i == num % When i = 2, j will restart to 1. Happens once b/c the subscripts we have for each coef is 11,12 and 21,22

                j = 1;
                i = i+1;

            else

               i = i+1;
               j = j+1;

            end            
        end

        denom_sum = zeros(1,num); % The denaminator for each i-subscript, in this case, it would be 2. 
        denom_sum(1) = denom_sum_comp(2); % Should have: (S11, A11 & S12, A12); Don't include denom_sum_comp(1) b/c S11 & A11; i =1
        denom_sum(2) = denom_sum_comp(3); % Should have: (S21, A21 & S22 A22); Don't include denom_sum_comp(4) b/c S22 & A22; i = 2

    elseif num == 3

        denom_sum_comp = zeros(1,num_coef);

        for w=1:length(denom_sum_comp)

            denom_sum_comp(w) = (S_coef(i)*A_coef(i))*(mf_a(j)/sqrt(mu_a(j)));

            if i == num || i==num*2  % When i = 3, j will restart to 1 and when i = 6, j will restart to 1. Happens twice b/c the subscripts we have for each coef is 11,12,13 ; 21,22,23 and 31, 32, 33

                j = 1;
                i = i+1;

            else

               i = i+1;
               j = j+1;

            end  
        end

        denom_sum = zeros(1,num); % The denaminator for each i-subscript, in this case, it would be 3. 
        denom_sum(1) = denom_sum_comp(2) + denom_sum_comp(3); % Should have: (S11, A11; S12, A12; S13, A13 ); Don't include denom_sum_comp(1) b/c S11 & A11; i =1
        denom_sum(2) = denom_sum_comp(4) + denom_sum_comp(6); % Should have: (S21, A21; S22, A22; S23, A23); Don't include denom_sum_comp(4) b/c S22 & A22; i = 2
        denom_sum(3) = denom_sum_comp(7) + denom_sum_comp(8); % ---

    elseif num == 4

        denom_sum_comp = zeros(1,num_coef);

        for w=1:length(denom_sum_comp)

            denom_sum_comp(w) = (S_coef(i)*A_coef(i))*(mf_a(j)/sqrt(mu_a(j)));

            if i == num || i==num*2 || i==num*3 % --

                j = 1;
                i = i+1;

            else

               i = i+1;
               j = j+1;

            end  
        end

        denom_sum = zeros(1,num); % The denaminator for each i-subscript, in this case, it would be 4. 
        denom_sum(1) = denom_sum_comp(2) + denom_sum_comp(3) + denom_sum_comp(4); % --
        denom_sum(2) = denom_sum_comp(5) + denom_sum_comp(7) + denom_sum_comp(8); % --
        denom_sum(3) = denom_sum_comp(9) + denom_sum_comp(10) + denom_sum_comp(12); % ---
        denom_sum(4) = denom_sum_comp(13) + denom_sum_comp(14) + denom_sum_comp(15); % --

    elseif num == 5

        denom_sum_comp = zeros(1,num_coef);

        for w=1:length(denom_sum_comp)

            denom_sum_comp(w) = (S_coef(i)*A_coef(i))*(mf_a(j)/sqrt(mu_a(j)));

            if i == num || i==num*2 || i==num*3 || i==num*4 % --

                j = 1;
                i = i+1;

            else

               i = i+1;
               j = j+1;

            end  
        end

        denom_sum = zeros(1,num); % The denaminator for each i-subscript, in this case, it would be 4. 
        denom_sum(1) = denom_sum_comp(2) + denom_sum_comp(3) + denom_sum_comp(4) + denom_sum_comp(5); % --
        denom_sum(2) = denom_sum_comp(6) + denom_sum_comp(8) + denom_sum_comp(9) + denom_sum_comp(10); % --
        denom_sum(3) = denom_sum_comp(11) + denom_sum_comp(12) + denom_sum_comp(14) + denom_sum_comp(15); % ---
        denom_sum(4) = denom_sum_comp(16) + denom_sum_comp(17) + denom_sum_comp(18) + denom_sum_comp(20); % --
        denom_sum(5) = denom_sum_comp(21) + denom_sum_comp(22) + denom_sum_comp(23) + denom_sum_comp(24); % --

    else
        error('Something is wrong... could not determine how many chemicals to sum...');

    end

    visc_mix = zeros(1,num);
    for w=1:length(visc_mix)

        visc_mix(w) = (mf_a(w)*sqrt(mu_a(w))) / ((mf_a(w)/sqrt(mu_a(w)))+denom_sum(w));
        %disp(((mf_a(w)/sqrt(mu_a(w)))+denom_sum(w)));
        %disp((mf_a(w)*sqrt(mu_a(w))));
    end

    visc_mix_gas = sum(visc_mix); % calculates the viscosity of the gas mixture at the 'w' reference temperature value
    
    visc_gas_mix_a(aaa) = visc_mix_gas; % storing the viscosity gas mixture value in the temperature (1-3500k) array. 

    %% ------- THERMAL CONDUCTIVITY GAS MIXTURE CALCULATION PART ---------

    
    %% Calculating unlike molecule interaction properties (therm_ij & visc_ij)

    % Requires
    %   - Omega (2,2)_ij
    %   - a & b parameters_ij
    %   - T*_ij
    %   - sigma_ij
    %   - e_ij

    % i are rows and j are columns 

    % Calculating sigma_ij values
    
    sigma_aa = zeros(num);

    for i=1:1:num
       for j=1:1:num 
           sigma_aa(i,j) = 0.5*(sigma_a(i)+sigma_a(j));
       end
    end

    % calculating e/k_ij values / ij or ji(k) 

    ek_aa = zeros(num);

    for i=1:num
        for j=1:num
            ek_aa(i,j) = sqrt(ek_a(i)*ek_a(j));
        end
    end

    % Calculating T* (kt/e_ij) values  / ij or ji 
    
    t_star = zeros(num); 
    t_star = temp*(1./ek_aa);
    
    % Calculate Omega(2,2)_ij (Imported from omega_func.m) - used for therm_ij & visc_ij / ij or ji

    omega_22 = zeros(num); 

    for w = 1:num*num

       x = t_star(w);
       omega_22(w) =  (1.586)+(-0.7882)*log(x)+(0.2938)*log(x)^2+...
                   (0.008756)*log(x)^3+(-0.05198)*log(x)^4+(0.01936)*log(x)^5+(-0.003264)*log(x)^6+...
                   (0.0002639)*log(x)^7+(-8.135*10^-6)*log(x)^8;
    end

    % Calculate Omega(1,2)_ij (Imported from omega_func.m) - used for b_parameter / ij or ji

    omega_12 = zeros(num);

    for w=1:num*num

       x = t_star(w);
       omega_12(w) = 1.204+(-0.5152)*log(x)+(0.2609)*log(x)^2+...
                    (-0.06649)*log(x)^3+(-0.01035)*log(x)^4+(0.01155)*log(x)^5+(-0.003077)*log(x)^6+...
                    (0.000366)*log(x)^7+(-1.671*10^-5)*log(x)^8; 
    end
    
    % Calculate Omega(1,3)_ij (Imported from omega_func.m) - used for b_parameter / ij or ji
    
    omega_13 = zeros(num);
    
    for w=1:num*num

        x = t_star(w);
        omega_13(w) = 1.076+(-0.3846)*log(x)+(0.2081)*log(x)^2+...
                      (-0.0752)*log(x)^3+(0.005667)*log(x)^4+(0.005235)*log(x)^5+(-0.001856)*log(x)^6+...
                      (0.0002466)*log(x)^7+(-1.199*10^-5)*log(x)^8;
    end
    
    % Calculate Omega(1,1)_ij (Imported from omega_func.m) - used for b_parameter / ij or ji

    omega_11 = zeros(num);

    for w=1:num*num

      x = t_star(w);
      omega_11(w) = 1.44+(-0.7037)*log(x)+(0.286)*log(x)^2+...
                    (-0.03118)*log(x)^3+(-0.02613)*log(x)^4+(0.0127)*log(x)^5+...
                    (-0.002519)*log(x)^6+(0.0002424)*log(x)^7+(-9.291*10^-6)*log(x)^8;
    end
    
    % A_parameter_ij is used in F_ij & Phi_ij coefficient
    
    a_parameter = zeros(num);

    for i=1:num
        for j=1:num
            a_parameter(i,j) = omega_22(i,j)/omega_11(i,j);
        end
    end

    % B_parameter_ij is used in F_ij & Phi_ij coefficient
    b_parameter = zeros(num);

    for i=1:num
        for j=1:num
            b_parameter(i,j) = (5*omega_12(i,j)-4*omega_13(i,j))/(omega_11(i,j));
        end
    end
    
    % Calculate visc_ij coef [Pa*s or kg/m*s] / ij or ji

    visc_ij = zeros(num); 

    for i = 1:num
        for j = 1:num
            visc_ij(i,j) = (266.93*(sqrt((2*mw_a(i)*mw_a(j)*temp)/(mw_a(i)+mw_a(j)))/((sigma_aa(i,j))^2*omega_22(i,j)))); % eq to solve 
            visc_ij(i,j) = visc_ij(i,j)*10^(-7)*0.1; % kg/m*s or Pa*s
        end
    end
    
    % Calculate therm_ij coef [W/m*k] orignially [cal/cm*s*c or cal/cm*s*k] / ij or ji

    therm_ij = zeros(num);
    num_therm = zeros(num);

    for i=1:num
        for j=1:num
             num_therm(i,j) = sqrt((temp*(mw_a(i)+mw_a(j)))/(2*mw_a(i)*mw_a(j)));
             therm_ij(i,j) = (1989.1*((num_therm(i,j))/((sigma_aa(i,j))^2*omega_22(i,j))));
             therm_ij(i,j) = therm_ij(i,j)*10^(-7)*418.4; % W/m*K
        end
    end
    
    %% Calculating  Phi_ij coefficient, sub_phi_ij coefficient & sub_phi_ji -- Used for viscosity/needed for thermal conductivity

    % Plugged into the Psi coefficient (sub_phi_ij coefficient) - currently g/cm*s
 
    sub_phi_ij_coef = zeros(num);
    mu_a = mu_a*(10^-4); % kg/m*s or Pa*s (should be 10^-5)
    
    for i = 1:num
        for j = 1:num

           sub_phi_ij_coef(i,j) = ((mu_a(i))/visc_ij(i,j))*((2*mw_a(j))/(mw_a(i)+mw_a(j))); 

        end
    end
    
    % sub_phi_ji 

    sub_phi_ji_coef = zeros(num);
    sub_phi_ji_coef = transpose(sub_phi_ij_coef);
    
    % testing that the sub_phi coefficients are corrcet (should be close to unity)
        
    test = zeros(num); % (test of phi coefficients) should all come out to around unity
    
    for i = 1:num
        for j = 1:num
     
            test(i,j) = (sqrt(sub_phi_ij_coef(i,j))+sqrt(sub_phi_ji_coef(i,j)))*(1+sqrt(sub_phi_ij_coef(i,j)*sub_phi_ji_coef(i,j)))^(-1);

        end
    end
    
    % Replaces the A-coef (Phi coefficient) -- SIMPLIFIED VERSION
    
    
    phi_coef = zeros(num);
    num_phi = zeros(num);
    denom_phi = zeros(num);

    for i=1:num
        for j=1:num

            num_phi(i,j) = (mw_a(i)*sqrt(sub_phi_ij_coef(i,j))-mw_a(j)*sqrt(sub_phi_ji_coef(i,j)));
            denom_phi(i,j) = (2*(mw_a(i)+mw_a(j))+mw_a(j)*sqrt(sub_phi_ji_coef(i,j)));
            phi_coef(i,j) = sub_phi_ij_coef(i,j)+(num_phi(i,j)/denom_phi(i,j))*sqrt(sub_phi_ij_coef(i,j));
        end
    end
    
    
    % Replaces the A-coef (Phi coefficient) -- COMPLEX/MOST ACCURATE VERSION
    
    %{
    phi_coef = zeros(num);
    num_phi = zeros(num);
    denom1_phi = zeros(num);
    denom2_phi = zeros(num);
    denom_phi = zeros(num);

    for i=1:num
        for j=1:num

            num_phi(i,j) = ((mw_a(i)*sqrt(sub_phi_ij_coef(i,j))-mw_a(j)*sqrt(sub_phi_ji_coef(i,j)))*sqrt(sub_phi_ij_coef(i,j)));
            denom1_phi(i,j) = (((3*a_parameter(i,j))*(mw_a(i)+mw_a(j)))/(5-3*a_parameter(i,j)));
            denom2_phi(i,j) = ((sqrt(sub_phi_ij_coef(i,j))+sqrt(sub_phi_ji_coef(i,j)))/(1+sqrt(sub_phi_ij_coef(i,j)*sub_phi_ji_coef(i,j))));
            phi_coef(i,j) = sub_phi_ij_coef(i,j)+(num_phi(i,j)/(denom1_phi(i,j)+(denom2_phi(i,j)*mw_a(j)*sqrt(sub_phi_ji_coef(i,j)))));

        end
    end
    %}
       
    %% Calculating  Psi_ij coefficient, sub_psi_ij coefficient & F_ij coefficient -- Used for thermal conductivity

    % f_coef_ij is used in Phi_ij coefficient

    f_coef_ij = zeros(num);
    bracket_ij = zeros(num);

    for i=1:num
        for j=1:num

            bracket_ij(i,j) =(((15/(4*a_parameter(i,j)))-1)*(mw_a(i)-mw_a(j))+(((3*b_parameter(i,j))/(2*a_parameter(i,j)))+(5/(8*a_parameter(i,j))))*mw_a(j));
            f_coef_ij(i,j) = 1+((mw_a(i)-mw_a(j))/(mw_a(i)+mw_a(j))^2)*(bracket_ij(i,j));
        end
    end
    
    %  f_coef_ji

    f_coef_ji = zeros(num);
    f_coef_ji = transpose(f_coef_ij);
    
    % Plugged into the Phi coefficent (sub Psi coefficient)
    
    sub_psi_coef_ij = zeros(num);

    for i =1:num
        for j=1:num
            sub_psi_coef_ij(i,j) = sub_phi_ij_coef(i,j)*f_coef_ij(i,j);
        end
    end
    
    %  sub_psi_coef_ji 

    sub_psi_coef_ji = zeros(num);
    sub_psi_coef_ji = transpose(sub_psi_coef_ij);
    
    % testing that the sub_psi coefficients are corrcet (should be close to unity)

    test2 = zeros(num);

    for i=1:num
        for j=1:num

            test2(i,j) = (sqrt(sub_psi_coef_ij(i,j))+sqrt(sub_psi_coef_ji(i,j)))*(1+sqrt(sub_psi_coef_ij(i,j)*sub_psi_coef_ji(i,j)))^(-1);

        end
    end
    
    %disp(test2);
    
    % Replaces the A-coef (Psi coefficient) 
    
    
    psi_coef = zeros(num);
    num_psi = zeros(num);
    denom_psi = zeros(num);

    for i =1:num
        for j=1:num

            num_psi(i,j) = ((sqrt(sub_psi_coef_ij(i,j))/f_coef_ij(i,j))-(sqrt(sub_psi_coef_ji(i,j))/f_coef_ji(i,j)));
            denom_psi(i,j) = ((((mw_a(i)+mw_a(j))^2)/(2.6*mw_a(i)*mw_a(j)))+(sqrt(sub_psi_coef_ji(i,j)/f_coef_ji(i,j))));

            psi_coef(i,j) = sub_psi_coef_ij(i,j)+(num_psi(i,j)/denom_psi(i,j))*sqrt(sub_psi_coef_ij(i,j));
        end
    end
    
    % Replaces the A-coef (Phi coefficient) -- COMPLEX/MOST ACCURATE VERSION
    
    %{
    psi_coef = zeros(num);
    num_psi = zeros(num);
    denom1_psi = zeros(num);
    denom2_psi = zeros(num);
    denom_psi = zeros(num);

    for i=1:num
        for j=1:num

            num_psi(i,j) = (((sqrt(sub_psi_coef_ij(i,j))/f_coef_ij(i,j))-(sqrt(sub_psi_coef_ji(i,j))/f_coef_ji(i,j)))*sqrt(sub_psi_coef_ij(i,j)));
            denom1_psi(i,j) = ((mw_a(i)+mw_a(j))^2/((mw_a(i)*mw_a(j))*((55/(8*a_parameter(i,j)))-((3*b_parameter(i,j))/(2*a_parameter(i,j)))-2)));
            denom2_psi(i,j) = ((sqrt(sub_psi_coef_ij(i,j))+ sqrt(sub_psi_coef_ji(i,j)))/(1+sqrt(sub_psi_coef_ij(i,j)*sub_psi_coef_ji(i,j))));
            denom_psi(i,j) = (denom1_psi(i,j) + (denom2_psi(i,j)*(sqrt(sub_psi_coef_ji(i,j))/f_coef_ji(i,j))));

            psi_coef(i,j) = sub_psi_coef_ij(i,j)+(num_psi(i,j)/denom_psi(i,j));

        end
    end
    %}
    
    %% Thermal Mixture Logic & Secondary Viscosity Logic

    % First, we must calculate the denaminator part that has the summation &
    % exclude i=j components

    denom_sum_comp = zeros(num);

    for i=1:num
        for j=1:num
            if j == i
                denom_sum_comp(i,j) = 0;
            else
                denom_sum_comp(i,j) = psi_coef(i,j)*mf_a(j);
            end
        end
    end

    denom_sum = sum(transpose(denom_sum_comp));

    % Second, we must obtain each thermal conductivity component. 

    therm_mix = zeros(1,num);

    for w=1:length(therm_mix)

       therm_mix(w) = (mf_a(w)*therm_a(w))/(mf_a(w) + denom_sum(w)); % in units of W/m*k

    end
    
    % Finally, we add 'em all up
    gas_therm = sum(therm_mix); % [W/m*k]
     
    % And now we store it 
    
    % If there are polar gases present, thermal conductivity will increase
    % by 10 times since that is about the difference between a non-polar
    % and polar thermal conductivity.
    
    polar_gas_logic = 0;
    dm_logic = (dm_a)/(3.335640*10^-30);
   
    for w=1:num
        if dm_logic(w) > 0.1
            
            polar_gas_logic = polar_gas_logic+1;
            
        elseif dm_logic(w) <= 0.1
            
            polar_gas_logic = polar_gas_logic;
     
        end
    end
    
    if polar_gas_logic ~= 0 
       
       gas_therm_a(aaa) = gas_therm*10; % [W/m*k]
       
    elseif polar_gas_logic == 0
       
       gas_therm_a(aaa) = gas_therm; % [W/m*k]
       
    end
    
    % Second, we must obtain each viscosity component
    %{
    visc_mix = zeros(1,num);
    
    for w=1:length(visc_mix)
        
        visc_mix(w) = (mf_a(w)*mu_a(w))/(mf_a(w) + denom_sum(w)); % in units of kg/m*s or Pa*S

    end
   
    % Finally, we add 'em all up  
    gas_visc = sum(visc_mix); % [Pa*s]
    
    %And now we store it
    gas_visc_a(aaa) = gas_visc*(10^4); % in units of 10^-5 Pa*S
    %}
    
    
    temp = temp+1; % the reference temperature, which continues to increase at each iteration, until it reaches 3500. 
end

temp_range = transpose(1:3500);
final_visc_gas_mix_a = transpose(visc_gas_mix_a);
final_therm_gas_mix_a = transpose(gas_therm_a);
%final_secondvisc_gas_mix_a = transpose(gas_visc_a);

%data_matrix = [temp_range,final_visc_gas_mix_a,final_therm_gas_mix_a,final_secondvisc_gas_mix_a];
data_matrix = [temp_range,final_visc_gas_mix_a,final_therm_gas_mix_a];
writematrix(data_matrix,'viscNtherm_range.txt');
