IF OBJECT_ID('tParameters') IS NOT NULL
TRUNCATE TABLE tParameters
IF EXISTS(SELECT * FROM dbo.sysobjects
   WHERE id = OBJECT_ID(N'[dbo].[FK_tParameters_FormID]') AND OBJECTPROPERTY(id, N'IsForeignKey') = 1)
ALTER TABLE [dbo].[tParameters] DROP CONSTRAINT FK_tParameters_FormID
TRUNCATE TABLE tRequestLog
ALTER TABLE [dbo].[tParameters] WITH CHECK ADD CONSTRAINT [FK_tParameters_FormID] FOREIGN KEY([FormID])
REFERENCES [dbo].[tRequestLog] ([FormID])