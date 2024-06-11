package main

import (
	"database/sql"
	"os"

	"github.com/joho/godotenv"
	"github.com/labstack/gommon/log"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Content struct {
	Id    int64  `json:"id" gorm:"primaryKey;autoIncrement"`
	Color string `json:"color"`
	Title string `json:"title"`
}

type Tabler interface {
	TableName() string
}

func (Content) TableName() string {
	return "content"
}

func ConnectDB() *gorm.DB {
	godotenv.Load(".env")
	mydb_dsn, ok := os.LookupEnv("DATABASE_URL")
	if !ok {
		panic("DATABASE_URL not found")
	}

	log.Info("Connecting to database: ", mydb_dsn)
	sqlDB, err := sql.Open("pgx", mydb_dsn)
	if err != nil {
		panic(err)
	}
	db, err := gorm.Open(postgres.New(postgres.Config{
		Conn: sqlDB,
	}), &gorm.Config{})

	if err != nil {
		panic(err)
	}
	return db
}
