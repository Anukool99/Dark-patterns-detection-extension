const express = require('express');
const cors = require('cors');
const { load } = require('joblib');

const app = express();
const port = 3000;

const presenceClassifier = load('presence_classifier.joblib');
const presenceVect = load('presence_vectorizer.joblib');
const categoryClassifier = load('category_classifier.joblib');
const categoryVect = load('category_vectorizer.joblib');

app.use(cors());
app.use(express.json());

app.post('/', (req, res) => {
  const output = [];
  const data = req.body.tokens;

  data.forEach((token) => {
    const result = presenceClassifier.predict(presenceVect.transform([token]));

    if (result === 'Dark') {
      const cat = categoryClassifier.predict(categoryVect.transform([token]));
      output.push(cat[0]);
    } else {
      output.push(result[0]);
    }
  });

  const dark = data.filter((_, i) => output[i] === 'Dark');
  console.log(dark);
  console.log();
  console.log(dark.length);

  const message = { result: output };
  console.log(message);

  res.json(message);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
