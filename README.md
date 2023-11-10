# Timesedler
<h4>Python projekt. Automatisk kopiering af timesedler fra mTidsStatistik til projektets bilagsmappe</h4>

<p>På baggrund af registreringerne i den Finansielle rapport, fanebladet ManedsStatistik, kopieres timesedler fra mTidsStatistik til projektets bilagsmappe.</p>

<ol>
    <li>ManedsStatik-tabellen indlæses som en dataframe</li>
    <li>df tilpasses og undersøges for diverse fejl</li>
    <ol>
        <li>Nan konvertes til 0</li>
        <li>Kolonner uniformeres ift datatyper</li>
        <li>Rækker hvor navne-cellen er lig 0 slettes</li>
        <li>Der oprettes en ny kolonne i df til navne-ini</li>
        <li>navne-ini udfyldes på baggrund af navne-kolonnen</li>
    </ol>
    <li>Der laves et udtræk af df for det relevante år</li>
    <li>Med udgangspunkt i udtrækket laves en navneliste - 'ini_måned_år'</li>
    <li>På baggrund af navnelisten kopieres - hvis filerne ikke findes i forvejen/eller overskrives? -  relevante timesedler fra mTidsStatistik</li>
    <ol>
        <li>Sti til source-mappen dannes - ROD-Classen, den er fælles for alle projekter</li>
        <li>Sti til destinations-mappen dannes - i den enkelte PROJEKT-CLASSE</li>
        <li>Det undersøges om timesedlen(.pdf-filen) findes i source-mappen</li>
        <li>Det undersøges om timesedlen(.pdf-filen) findes i destrinations-mappen</li>
		<li>Hvis timesedlen findes i source-mappen og den skal kopieres(enten ikke-findes/ønskes overskrevet) - kopieres filen til dest-mappen<li> 
    </ol>


</ol>

