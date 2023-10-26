<!DOCTYPE html>
<html>
  <head>
    <title>Music Generation with Meta AI's MusicGen</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="helper-v2.js" defer></script>
    <style>
      td {
        vertical-align: middle;
      }
      audio {
        width: 20vw;
        min-width: 100px;
        max-width: 250px;
      }
      .timestamp-label {
        color: gray;
      }
      table.wide-audio audio {
        width: 40vw;
        max-width: 40vw;
      }
    </style>
  </head>
  <body>
    <div class="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded">
      <div class="text-center">
        <h1>MusicGen: Generating Music From Text-Prompt</h1>
        <p class="lead fw-bold">
          |<a
            href="https://github.com/nsaintsever/music-generation"
            class="btn border-white bg-white fw-bold"
            >My Github Repo</a
          >|
        </p>
        <p class="fst-italic mb-0">
          Nicolas Saint Sever
        </p>
        <p>Personnal project</p>
      </div>
      <p>
        <b>Abstract</b>
        Text to Music Generation App built using Meta's Audiocraft library (MusicGen model). It is a Streamlit application utilises Music Gen small model.
        You'll find below a few extracts of generated music through a text prompt.
        You'll also find a live demonstration of the streamlit app as I've only used this web-app locally.
      </p>
    </div>
<div class="container pt-5 mt-5 shadow p-5 mb-5 bg-white rounded">
  <h3>Songs generated</h3>
  <div class="container pt-3">
    <div class="table-responsive pt-3">
      <table class="table pt-2 wide-audio" id="longgen-generation">
        <thead>
          <tr>
            <th>Text prompt</th>
            <th style="text-align: right">Generated audio</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Text prompt 1</td>
            <td>
              <audio controls>
                <source src="lien_audio_1.mp3" type="audio/mpeg">
                Votre navigateur ne supporte pas l'élément audio.
              </audio>
            </td>
          </tr>
          <tr>
            <td>Text prompt 2</td>
            <td>
              <audio controls>
                <source src="lien_audio_2.mp3" type="audio/mpeg">
                Votre navigateur ne supporte pas l'élément audio.
              </audio>
            </td>
          </tr>
          <tr>
            <td>Text prompt 3</td>
            <td>
              <audio controls>
                <source src="lien_audio_3.mp3" type="audio/mpeg">
                Votre navigateur ne supporte pas l'élément audio.
              </audio>
            </td>
          </tr>
          <tr>
            <td>Text prompt 4</td>
            <td>
              <audio controls>
                <source src="lien_audio_4.mp3" type="audio/mpeg">
                Votre navigateur ne supporte pas l'élément audio.
              </audio>
            </td>
          </tr>
          <tr>
            <td>Text prompt 5</td>
            <td>
              <audio controls>
                <source src="lien_audio_5.mp3" type="audio/mpeg">
                Votre navigateur ne supporte pas l'élément audio.
              </audio>
            </td>
          </tr>
          <tr>
            <td>Text prompt 6</td>
            <td>
              <audio controls>
                <source src="lien_audio_6.mp3" type="audio/mpeg">
                Votre navigateur ne supporte pas l'élément audio.
              </audio>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
