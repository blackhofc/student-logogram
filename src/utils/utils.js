// Import data
import students from "../Files/students.json";
import symbols from "../Files/translations.json";

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


function isW(message) {
    const result = []
    message.toString().split(' ').forEach((value) =>{
        result.push({ type: 'word', value })
    });
    return result;
}

function isL(value) {
    return { type: 'logogram', value };
}

function processGrams(msg, grams) {
    const result = [];
    Object.entries(grams || {}).forEach(([key, value]) => {
        if (result.length === 0) {
            result.push(...msg);
        }
        result.push(...isW(key), isL(value.id));
    });
    return result;
}

function describeStudent(student) {
    if (!student) {
        return [];
    }

    const { name, age, grams, music_genres } = student;

    const nameToken = isW(name.split(" ")[0]);
    const ageToken = isW(age);
    const genderTokens = processGrams([], grams?.gender);
    const genresTokens = music_genres ? [...isW('escucha género'), ...isW(music_genres.join(', '))] : [];
    const sportsTokens = processGrams(isW('y le gusta mirar'), grams?.fav_sports);
    const languagesTokens = processGrams(isW('habla en'), grams?.languages);

    console.log('Description', [...nameToken, ...isW('es'), ...genderTokens, ...isW('tiene'), ...ageToken, ...isW('años'), ...languagesTokens, ...genresTokens, ...sportsTokens])
    return [...nameToken, ...isW('es'), ...genderTokens, ...isW('tiene'), ...ageToken, ...isW('años'), ...languagesTokens, ...genresTokens, ...sportsTokens];
}

function loadStudents(selectedId){
    const parsedStudents = [];
    // students.sort((a, b) => a.name.localeCompare(b.name));
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
        symbol: `/images/logograms/${id}.png`,
        symbolBig: `/images/logograms/big_${id}.png`,
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

function extractParams(window) {
    const path = window.location.pathname;
    const segments = path.split('/');
    const id = segments[segments.length - 1];
    return { id };
}

export {
    VARIABLES,
    describeStudent,
    loadStudents,
    logogramSymbols,
    extractParams
}
