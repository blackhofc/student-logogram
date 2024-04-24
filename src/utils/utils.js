// Import data
import students from "../students.json";
import symbols from "../translations.json";

const VARIABLES = {
    gender: { title: "Género", description: "Ubicado a 90°", data: symbols.gender },
    /*age: {
      title: "Age",
      description: "Gender symbol size",
      data: symbols.age
    }, */
    music_genres: {
      title: "Intereses Musicales",
      description: "Gradiente del logograma",
      data: symbols.music_genres
    },
    fav_sports: {
      title: "Deportes Favoritos",
      description: "Ubicados a 135°, 180°, 225°",
      data: symbols.fav_sports
    },
    languages: { title: "Idiomas", description: "Ubicados a 0°, 45°, 315°", data: symbols.languages },
};

function minIcon(){
    
    // <img class="image-container-logogram" src={icon} alt="" />
    return ''
}

function describeStudent(student) {
    if(!student){
        return;
    }

    const name = student.name.split(" ")[0];
    const gender = student.gender;
    const age = student.age;
    const genres = student.music_genres.join(", ");
    const sports = student.fav_sports.join(", ");
    const languages = student.languages.join(", ");

    return `${name} es ${gender}, tiene ${age} años, escucha genero ${genres}, le gusta mirar ${sports} y habla en ${languages}.`;
  }

function loadStudents(selectedId){
    const parsedStudents = [];
    students.sort((a, b) => a.name.localeCompare(b.name));
    students.forEach((person) => {
        const { id, name, age, gender, music_genres, fav_sports } = person;

        const defaultColor = "#000"; // Default color if music genres are not available
        let colors;

        if (music_genres.length === 0) {
        // If no music genres are available, duplicate the default color
        colors = [defaultColor, defaultColor];
        } else if (music_genres.length === 1) {
        // If there's only one music genre, duplicate the unique color
        colors = [music_genres[0], music_genres[0]].map(
            (genre) =>
            `#${
                symbols["music_genres"][genre]?.color ||
                symbols["music_genres"]["Otros"].color
            }`
        );
        } else {
        colors = music_genres.map(
            (genre) =>
            `#${
                symbols["music_genres"][genre]?.color ||
                symbols["music_genres"]["Otros"].color
            }`
        );
        }
        const selected = selectedId === id;
        // console.log(selectedId, id, selected);

        parsedStudents.push({
        ...person,
        grams: logogramSymbols(person),
        symbol: `./images/logograms/${id}.png`,
        gradient: colors.join(", "),
        selected
        });

    });
    return parsedStudents;
}

// Icons of a student, foreach
function logogramSymbols(student) {
    if (!student) return [];

    const variables = {
        gender: {[student.gender]: symbols.gender[student.gender]},
        /*music_genres: Object.fromEntries(
            Object.entries(symbols.music_genres)
                .filter(([genre]) => student.music_genres.includes(genre))
                .map(([genre, data]) => [genre, data])
        ), */
        fav_sports: Object.fromEntries(
            Object.entries(symbols.fav_sports)
                .filter(([sport]) => student.fav_sports.includes(sport))
                .map(([sport, data]) => [sport, data])
        ),
        languages: Object.fromEntries(
            Object.entries(symbols.languages)
                .filter(([lang]) => student.languages.includes(lang))
                .map(([lang, data]) => [lang, data])
        )
    };

    return variables;
}

export {
    VARIABLES,
    describeStudent,
    loadStudents,
    logogramSymbols
}
