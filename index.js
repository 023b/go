const simpleGit = require("simple-git");
const jsonfile = require("jsonfile");
const moment = require("moment");
const random = require("random");
const FILE_PATH = "./data.json";
const git = simpleGit();

const makeCommit = async (startDate, endDate, commitsPerDay = 5) => {
  const current = moment(startDate);
  const end = moment(endDate);

  while (current.isBefore(end)) {
    const date = current.format();
    const data = { date };
    await jsonfile.writeFile(FILE_PATH, data);

    for (let i = 0; i < commitsPerDay; i++) {
      await git.add(FILE_PATH);
      await git.commit(`Commit on ${date}`, { "--date": date });
    }

    current.add(1, "day");
  }

  await git.push();
  console.log("Pushed all commits!");
};

makeCommit("2024-04-01", moment().format("YYYY-MM-DD"));
