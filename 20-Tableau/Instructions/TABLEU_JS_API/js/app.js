$(document).ready(function() {
    initializeViz();

});

function initializeViz() {
    var placeholderDiv = document.getElementById("tableauViz");
    var url = "https://public.tableau.com/views/CitiBikeTripAnalytics_15990127189300/CitiBikeTripAnalytics";
    var options = {
        width: placeholderDiv.offsetWidth,
        height: placeholderDiv.offsetHeight,
        hideTabs: false,
        hideToolbar: false,
        onFirstInteractive: function() {
            workbook = viz.getWorkbook();
            activeSheet = workbook.getActiveSheet();
        }
    };
    viz = new tableau.Viz(placeholderDiv, url, options);
}