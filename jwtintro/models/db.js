//https://sequelize.org/master/manual/dialect-specific-things.html

const { Sequelize, DataTypes } = require('sequelize');

const sequelize = new Sequelize('soccerz', 'postgres', 'postgres', {
    dialect: 'postgres',
    dialectOptions: {
      // Your pg options here
    },
    host: 'localhost',
    port: 5432
  });

  // no PK lets sequelize create its own pk as type SERIAL
  const Player = sequelize.define('Player', {
    // Model attributes are defined here
    name: {
      type: DataTypes.STRING,
      allowNull: false
    },
    birthday: {
      type: DataTypes.DATEONLY
      // allowNull defaults to true
    },
    position: {
        type:DataTypes.STRING
    }
  }, {
    // Other model options go here
  });

  const Team = sequelize.define('Team',{
    name:{
        type: DataTypes.STRING(100),
        allowNull: false
    }
  });

  const Game = sequelize.define('Game',{
    time:{
        type:DataTypes.DATE,
        primaryKey:true
    },
    teamA:{
        type:DataTypes.INTEGER,
        references: {
            model: Team,
            key: 'id'            
        }
    },
    teamB:{
        type:DataTypes.INTEGER,
        references: {
            model: Team,
            key: 'id'            
        }
    },
    goalsA:{
        type:DataTypes.INTEGER
    },
    goalsB:{
        type:DataTypes.INTEGER
    }
  });

  sequelize.sync();