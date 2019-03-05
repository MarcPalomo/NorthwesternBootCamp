Sub Volume():

' declare the variable for worksheet
Dim ws As Worksheet

' set the ability to apply code for each worksheet

For Each ws In Worksheets

' declare the variables that will be used to reference the ticker and the volume

Dim TickerName As String
Dim Volume As Double

' declare the variables for the necessary components to reference when the ticker changes in order to get the opening and closing price as well as the current ticker, next ticker, and previous ticker

Dim YearlyChange As Double
Dim Opening As Double
Dim Closing As Double
Dim NextTicker As String
Dim PreviousTicker As String
Dim PercentageChange As Double

' declare a variable to establish where the table information will get placed

Dim SummaryTableRow As Integer
SummaryTableRow = 1

' add the table headers
ws.Range("I1").Value = "Ticker"
ws.Range("J1").Value = "Yearly Change"
ws.Range("K1").Value = "Percent Change"
ws.Range("L1").Value = "Total Stock Volume"

' start the for-loop to go through all the data and assign data to the variable
' NextTicker takes the ticker symbol of the proceeding row
' PreviousTicker takes the ticker symbol of the previous row
' TickerName takes the ticker symbol of the current row
' Volume is being calculated by adding up the previous volume total and the current row’s volume total

For i = 2 To ws.Cells(Rows.Count, 1).End(xlUp).Row
    NextTicker = ws.Cells(i + 1, 1)
    PreviousTicker = ws.Cells(i - 1, 1)
    TickerName = ws.Cells(i, 1).Value
    Volume = Volume + ws.Cells(i, 7).Value
    
    ' using the If statement to identify when data needs to be added to the table based on information in the current row of the for-loop or a previously referenced variable

    If TickerName <> NextTicker Then
        SummaryTableRow = SummaryTableRow + 1
        
        Closing = ws.Cells(i, 6).Value
        ws.Range("I" & SummaryTableRow).Value = TickerName
        ws.Range("L" & SummaryTableRow).Value = Volume
        YearlyChange = Closing - Opening
        ws.Range("J" & SummaryTableRow).Value = YearlyChange

    ' reset the volume so that the next ticker starts to calculate the total volume for the year starting at 0
        Volume = 0

    ' this will do the color formatting based on YearlyChange being less or greater to 0. The instructions do not mention anything about equaling zero, so a cell that is exactly 0 will have no color.

            If YearlyChange > 0 Then
                ws.Range("J" & SummaryTableRow).Interior.ColorIndex = 4
            ElseIf YearlyChange < 0 Then
                ws.Range("J" & SummaryTableRow).Interior.ColorIndex = 3
            End If

    ' i needed to change this opening function slightly because dividing by 0 is problematic in the event a stock opened the year at 0.

        If Opening <> 0 Then
            PercentageChange = YearlyChange / Opening
        Else
            PercentageChange = 0
        End If

    ' add the PercentageChange to the summary table

        ws.Range("K" & SummaryTableRow).Value = PercentageChange

    
    ElseIf PreviousTicker <> TickerName Or i = 2 Then
    ' the opening will come from the first row of a given ticker and we need to set it when we get to that first row because we need to reference it later
        Opening = ws.Cells(i, 3).Value
        
    
    End If

' closes the for-loop
Next i

' adds the format 0.00% to just clean up the data a little
ws.Range("K1:K" & ws.Cells(Rows.Count, 1).End(xlUp).Row).NumberFormat = "0.00%"


' sets new headers to columns and rows in the table for the hard exercise
ws.Range("O2").Value = "Greatest % Increase"
ws.Range("O3").Value = "Greatest % Decrease"
ws.Range("O4").Value = "Greatest Total Volume"
ws.Range("P1").Value = "Ticker"
ws.Range("Q1").Value = "Value"

' declares new variables for the Max and Min values
Dim Max As Double
Dim Min As Double

' identifies the max in column K across all worksheets. since K is the same in each worksheet it is referenced specifically. I realize I could have used a variable since I repeat the finding last row column in multiple places, but i kept it written out to show my work in identifying the rows of the given max and mins

' this finds the actual max and min values and assigns them to the variables
Max = Application.WorksheetFunction.Max(ws.Range("K2:K" & ws.Cells(Rows.Count, 1).End(xlUp).Row))
Min = Application.WorksheetFunction.Min(ws.Range("K2:K" & ws.Cells(Rows.Count, 1).End(xlUp).Row))


' i created new variables to identify the rows in order to reference the ticker for the max and mins found to complete the new chart

Dim MaxTikRow As Integer
Dim MinTikRow As Integer


' these match formulas identify the rows of the max and min and assign them to the variable to be referenced in placing the ticker information in the new chart

MaxTikRow = WorksheetFunction.Match(Application.WorksheetFunction.Max(ws.Range("K2:K" & ws.Cells(Rows.Count, 1).End(xlUp).Row)), ws.Range("K2:K" & ws.Cells(Rows.Count, 1).End(xlUp).Row), 0)
MinTikRow = WorksheetFunction.Match(Application.WorksheetFunction.Min(ws.Range("K2:K" & ws.Cells(Rows.Count, 1).End(xlUp).Row)), ws.Range("K2:K" & ws.Cells(Rows.Count, 1).End(xlUp).Row), 0)

' declare new variables to complete the last item in the new chart for volume
Dim MaxVolume As Double
Dim MaxVolumeRow As Integer

' assigns the max volume and the max volume row in order to reference the ticker name later
MaxVolume = Application.WorksheetFunction.Max(ws.Range("L2:L" & ws.Cells(Rows.Count, 1).End(xlUp).Row))
MaxVolumeRow = WorksheetFunction.Match(Application.WorksheetFunction.Max(ws.Range("L2:L" & ws.Cells(Rows.Count, 1).End(xlUp).Row)), ws.Range("L2:L" & ws.Cells(Rows.Count, 1).End(xlUp).Row), 0)

' these place the appropriate Max, Min, and corresponding ticker name values into the new chart
ws.Range("P2").Value = ws.Cells(MaxTikRow + 1, 9)
ws.Range("Q2").Value = Max
ws.Range("P3").Value = ws.Cells(MinTikRow + 1, 9)
ws.Range("Q3").Value = Min
ws.Range("Q2:Q3").NumberFormat = "0.00%"
ws.Range("P4").Value = ws.Cells(MaxVolumeRow + 1, 9)
ws.Range("Q4").Value = MaxVolume

' this allows me to just clean everything up a bit by auto-fitting each column on each worksheet.
ws.Cells.EntireColumn.AutoFit

' this closes out the for-each that lets the code applied above using the ws added to the appropriate referenced cells and ranges to get repeated on each worksheet

Next ws



End Sub