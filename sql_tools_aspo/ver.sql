if exists (select 1 FROM sysobjects WHERE NAME = 'vVersionsNumbers')
Begin
if exists (select 1 from vVersionsNumbers where Versions = '3.1.1.6')
  select 'версия БД 3.1.1.6 или выше'
 else if exists (select 1 from vVersionsNumbers where Versions = '3.1.1.5')
  select 'версия БД 3.1.1.5'
 else if exists (select 1 from vVersionsNumbers where Versions = '3.1.1.4')
  select 'версия БД 3.1.1.4'
 else if exists (select 1 from vVersionsNumbers where Versions = '3.1.1.3')
  select 'версия БД 3.1.1.3'
 else if exists (select 1 from vVersionsNumbers where Versions = '3.1.1.2')
  select 'версия БД 3.1.1.2'
 else if exists (select 1 from vVersionsNumbers where Versions = '3.1.1.1_BETA')
  select 'версия БД 3.1.1.1_BETA'
 else if exists (select 1 from vVersionsNumbers where Versions = '3.1.0.4')
  select 'версия БД 3.1.0.4'
 else if exists (select 1 from vVersionsNumbers where Versions = '2.8.2.29')
  select 'версия БД 2.8.2.29'
 else if exists (select 1 from vVersionsNumbers where Versions = '2.8.2.28')
  select 'версия БД 2.8.2.28'
 else if exists (select 1 from vVersionsNumbers where Versions = '2.8.2.26_BETA')
  select 'версия БД 2.8.2.26_BETA'
 else if exists (select 1 from vVersionsNumbers where Versions = '2.8.2.25')
  select 'версия БД 2.8.2.25'
 else if exists (select 1 from vVersionsNumbers where Versions = '2.8.2.23')
  select 'версия БД 2.8.2.23'
 else if exists (select 1 from vVersionsNumbers where Versions = '2.8.2.22')
  select 'версия БД 2.8.2.22'
End
else if exists(select 1 from tDefaultParams where ParamID = '691')
  select 'версия БД 2.8.2.20_BETA(21_BETA)'
else if exists(select 1 from tDefaultParams where ParamID = '683')
  select 'версия БД 2.8.2.18(181)'
else if exists(select 1 from sysobjects where name = 'dtIIPExams')
  select 'версия БД 2.8.2.17_ALPHA'
else if exists(select 1 from sysobjects where name = 'tRemoteErrLog')
  select 'версия БД 2.8.2.16'
else if exists(select 1 from vParams where ParamClassID = '1645')
  select 'версия БД 2.8.2.14(15_GAMMA)'
else if exists(select 1 from tDefaultParams where ParamID = '676')
  select 'версия БД 2.8.2.13_BETA'
else if exists(select 1 from vAlcoModels where AlcoModelID = '9')
  select 'версия БД 2.8.2.11_ALPHA (12_ALPHA)'
else if exists(select 1 from tDefaultParams where ParamID = '674')
  select 'версия БД 2.8.2.9_BETA (10_ALPHA)'
else IF OBJECT_ID('vRemoteExamsMsg') IS not NULL
	BEGIN
 IF exists(select 1 from vRemoteExamsMsg where MsgID = '19')
  select 'версия БД 2.8.2.6_ALPHA'
	END
else if exists(select 1 from tDefaultParams where ParamID = '661')
  select 'версия БД 2.8.2.1_ALPHA'
else if exists(select 1 from sysobjects where name = 'tExamADParameters')
  select 'версия БД 2.8.1.12_ALPHA (2.8.1.13_ALPHA, 14_ALPHA, 15_ALPHA, 16_ALPHA)'
else if exists(select 1 from tDefaultParams where ParamName = 'CAPDOptions')
  select 'версия БД 2.8.1.4-2.8.1.11_ALPHA'
else if exists(select 1 from sysobjects where name = 'tSSPSExchangeRoads')
  select 'версия БД 2.8.1.3'
else if exists(select 1 from vAlcoModels where AlcoModelID = '6')
  select 'версия БД 2.8.1.1'
else if exists(select 1 from sysobjects where name = 'SP_GetUserASUTInfo')
  select 'версия БД 2.8.1.0'
else if exists(select 1 from sysobjects where name = 'tExamCalculated')
  select 'версия БД 2.8.0.097_BETA'
else if exists(select 1 from tLocalParams where ParamName = 'PswMode1')
  select 'версия БД 2.8.0.096'
else if exists(select 1 from tLocalParams where ParamName = 'LogXMLStoredTime')
  select 'версия БД 2.8.0.095'
else if exists(select 1 from sysobjects where name = 'SP_fNewMRPsw')
  select 'версия БД 2.8.0.094_BETA'
else if exists(select 1 from sysobjects where name = 'SP_RemoteToPrint')
  select 'версия БД 2.8.0.093'
else if exists(select 1 from sysobjects where name = 'SP_ASUTNeedSynchro')
  select 'версия БД 2.8.0.092'
else if exists(select 1 from tDefaultParams where ParamName = 'ShowExamUserRequest')
  select 'версия БД 2.8.0.091_BETA'
else if exists(select 1 from sysobjects where name = 'vNiValues')
  select 'версия БД 2.8.0.089(090)_BETA'
else if exists(select 1 from vStrings where StringID = '304'
        and String Like 'С сервера АСУ СПС не поступили данные о составе бригады%')
  select 'версия БД 2.8.0.088_BETA'
else if exists(select 1 from vCaptionsCorrect where NewCaption = 'RPi')
  select 'версия БД 2.8.0.086'
else if exists(select 1 from vFormTypes where FormTypeID= '48')
  select 'версия БД 2.8.0.083(084 или 2.8.0.085_BETA)'
else if exists(select 1 from sysobjects where name = 'tErrorIDs')
  select 'версия БД 2.8.0.081_BETA'
else if exists(select 1 from tLocalParams where ParamName = 'SSPSMLStoredPeriod')
  select 'версия БД 2.8.0.078_BETA или 2.8.0.079_BETA или 2.8.0.080_BETA'
else if exists(select 1 from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'tNodesDetails'
                and COLUMN_NAME  = 'TCPExchange')
  select 'версия БД 2.8.0.077_BETA'
else if exists(select 1 from tDefaultParams where ParamName = 'MaxPressLevel')
  select 'версия БД 2.8.0.076'
else if exists(select 1 from tLocalParams where ParamName = 'ViewSRPVColumn')
  select 'версия БД 2.8.0.075'
else if exists(select 1 from tDefaultParams where ParamName = 'SSSRWarningBlink')
  select 'версия БД 2.8.0.071'
else if exists(select 1 from tDefaultParams where ParamName = 'RemotePyroRetryCount')
  select 'версия БД 2.8.0.067'
else if exists(select 1 FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_NAME = 'dwUsersNames'
                AND TABLE_SCHEMA = 'dbo')
  select 'версия БД 2.8.0.065'
else if exists(select 1 from tDefaultParams where ParamName = 'RemoteConnectionQuality')
  select 'версия БД 2.8.0.060'
else if exists(select 1 from tDefaultParams where ParamName = 'SSPS Server')
  select 'версия БД 2.8.0.059'
else if exists(select 1 from tDefaultParams where ParamName = 'SkipDispFullAfter')
  select 'версия БД 2.8.0.058'
else if exists(select 1 from tDefaultParams where ParamName = 'JupiterDeviceName')
  select 'версия БД 2.8.0.057 BETA'
else if exists(select 1 from tDefaultParams where ParamName = 'JupiterCOMAutoFind')
  select 'версия БД 2.8.0.055'
else if exists(select 1 from tDefaultParams where ParamName = 'CanAlcoOnly')
  select 'версия БД 2.8.0.050'
else if exists(select 1 from tDefaultParams where ParamName = 'VChat')
  select 'версия БД 2.8.0.044'
else if exists(select 1 from tDefaultParams where ParamName = 'IronLogicZ2Port')
  select 'версия БД 2.8.0.035'
else if exists(select 1 from tDefaultParams where ParamName = 'VisibleHelp')
  select 'версия БД 2.8.0.016'
else if exists(select 1 from sysobjects where name = 'tNarkoCancelData')
  select 'версия БД 2.8.0.013'
else if exists(select 1 from tDefaultParams where ParamName = 'ForeignUsers')
  select 'версия БД 2.8.0.012'
else if exists(select 1 from tDefaultParams where ParamName = 'NarkoDefaultType')
  select 'версия БД 2.8.0.002'
else if exists(select 1 from tDefaultParams where ParamName = 'Signature Options')
  select 'версия БД 2.7.0.996'
else if exists(select 1 from tDefaultParams where ParamName = 'SaveRawMeasurementData')
  select 'версия БД 2.7.0.975'
else if exists(select 1 from tDefaultParams where ParamName = 'DACZeroTimeReset')
  select 'версия БД 2.7.0.973'
else if exists(select 1 from tDefaultParams where ParamName = 'ECGSaveLength')
  select 'версия БД 2.7.0.967'
else if exists(select 1 from sysobjects where name = 'SP_EKGFiltersLoad')
  select 'версия БД 2.7.0.950'
else if exists(select 1 from tDefaultParams where ParamName = 'LogEnable')
  select 'версия БД 2.7.0.930(931)'
else if exists(select 1 from tDefaultParams where ParamName = 'CardReaderRule')
  select 'версия БД 2.7.0.920'
else if exists(select 1 from tDefaultParams where ParamName = 'HideDecisionPFS')
  select 'версия БД 2.7.0.900(902,905)'
else if exists(select 1 from tDefaultParams where ParamName = 'BubbleOptions')
  select 'версия БД 2.7.0.897'
else if exists(select 1 from tDefaultParams where ParamName = 'UseStratification')
  select 'версия БД 2.7.0.889'
else if exists(select 1 from sysobjects where name = 'SP_GetMyNID')
  select 'версия БД 2.7.0.883'
else if exists(select 1 from tDefaultParams where ParamName = 'DefaultMedNodes')
  select 'версия БД 2.7.0.879'
else if exists(select 1 from sysobjects where name = 'SP_ExchangeStop')
  select 'версия БД 2.7.0.868'
else if exists(select 1 from tLocalParams where ParamName = 'DelNIDParent')
  select 'версия БД 2.7.0.866'
else if exists(select 1 from tDefaultParams where ParamName = 'CardReaderType')
  select 'версия БД 2.7.0.863(864)'
else if exists(select 1 from tDefaultParams where ParamName = 'CardReader')
  select 'версия БД 2.7.0.834'
else if exists(select 1 from tDefaultParams where ParamName = 'UseWorkOverflow')
  select 'версия БД 2.7.0.817'
else if exists(select 1 from tDefaultParams where ParamName = 'TemperAxsl')
  select 'версия БД 2.7.0.804(805)'
else if exists(select 1 from tDefaultParams where ParamName = 'LogPath')
  select 'версия БД 2.7.0.771'
else if exists(select 1 from tDefaultParams where ParamName = 'PulseLevelZoomView')
  select 'версия БД 2.7.0.736'
else if exists(select 1 from tDefaultParams where ParamName = 'DlgUserFilterChecked')
  select 'версия БД 2.7.0.730(731)'
else if exists(select 1 from tDefaultParams where ParamName = 'ResumeStateMode')
  select 'версия БД 2.7.0.723'
else if exists(select 1 from tDefaultParams where ParamName = 'EmuleCollectorAllowed')
  select 'версия БД 2.7.0.710(711)'
else if exists(select 1 from vDefaults where DefaultID = 52)
  select 'версия БД 2.7.0.694'
else if exists(select 1 from tDefaultParams where ParamName = 'Selectors')
  select 'версия БД 2.7.0.682'
else if exists(select 1 from tDefaultParams where ParamName = 'ResetResViewOnEWM')
  select 'версия БД 2.7.0.661'
else if exists(select 1 from vFormTypes where FormTypeID = 502)
  select 'версия БД 2.7.0.647(652)'
else if exists(select 1 from tDefaultParams where ParamName = 'RegistryPattern')
  select 'версия БД 2.7.0.642'
else if exists(select 1 from tDefaultParams where ParamName = 'SCardReaderName' and ParamType = 11)
  select 'версия БД 2.7.0.626'
else if exists(select 1 from tDefaultParams where ParamName = 'ShowMeasResIN')
  select 'версия БД 2.7.0.610'
else if exists(select 1 from tDefaultParams where ParamName = 'ServicePath')
  select 'версия БД 2.7.0.582(581)'
else if exists(select 1 from sysobjects where name = 'vNU4template')
  select 'версия БД 2.7.0.574'
else if exists(select 1 from tDefaultParams where ParamName = 'AISA' and Alias is not null)
  select 'версия БД 2.7.0.571'
else if exists(select 1 from tDefaultParams where ParamName = 'TimeOutPermitExams')
  select 'версия БД 2.7.0.570'
else if exists(select 1 from tDefaultParams where ParamName = 'BillDaysMax')
  select 'версия БД 2.7.0.510'
else if exists(select 1 from tDefaultParams where ParamName = 'WorkNodeTypeID')
  select 'версия БД 2.7.0.473'
else if exists(select 1 from sysobjects where name = 'dbo.UF_GetRRTime')
  select 'версия БД 2.7.0.464'
else if exists(select 1 from tDefaultParams where ParamName = 'ScrollUserListDelay')
  select 'версия БД 2.7.0.432'
else if exists(select 1 from tDefaultParams where ParamName = 'MeasFormExamUI')
  select 'версия БД 2.7.0.422 или ниже'
else
  select 'версия не определена, возможго БД 2.688.1.404 или ниже'
GO