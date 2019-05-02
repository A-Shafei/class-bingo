from bs4 import BeautifulSoup
from random import randint

html_doc = """
<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardl">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
      <td class="field">1</td>
    </tr>
    <tr>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
      <td class="field">2</td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>

<div class="cardr">
  <span class="title">Dr. Anwer Bingo</span>
  <table>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
    <tr>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
      <td class="field"></td>
    </tr>
  </table>
</div>
"""

# hardWords = ["Invest", "Investigate", "نعمل Experiment", "Bizarre"]
#
# soup = BeautifulSoup(html_doc, "lxml")
#
# tables = soup.find_all("table")
#
#
# for table in tables:
#
#     hardWord = hardWords[randint(0, 3)]
#
#     fields = table.find_all("td")
#     for field in fields:
#         if hardWord in field.strings:
#             hardField = field
#
#     middleField = fields[12]
#
#     hand = hardField.contents
#     hardField.contents = middleField.contents
#     middleField.contents = hand
#
#
# print(str(soup))

phrases = ["Punchline","N..n..n.. No No","The System is Well Understood","ده trackال","Assessment","Intuition","حقيقة الأمر","Problem-solving Skills","We Don't Know","Maneuver","Invest","Investigate","Scale Up","Scale Down","Projector","*Pause*.. Okay.","Information","Misleading","نعمل Experiment","Bizarre","*Psychedelic Tangent*","Consistent","Skimming","Treatment","Global View","*Pause*.. اسمك ايه؟","Good Point","This is a Good Question","ده lineال","Ad Hoc","Formalism"]

soup = BeautifulSoup(html_doc, "lxml")

tables = soup.find_all("table")



for table in tables:
	copied = phrases.copy()
	fields = table.find_all("td")
	for field in fields:
		field.string = copied.pop(randint(0,len(copied)-1))

print(str(soup))
