package main

import (
	"log/slog"
	"os"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/joho/godotenv"
)

func main() {
	e := echo.New()
	err := godotenv.Load(".env")
	if err != nil {
		slog.Info(".env file not found, using default values")
	}

	port := ":1323"
	if val, ok := os.LookupEnv("FUNCTIONS_CUSTOMHANDLER_PORT"); ok {
        port = ":" + val
    }


	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	e.GET("api/hello", SayHello)

	// CRUD operations
	e.POST("/api/content", CreateResource)
	e.GET("/api/content", ReadResource)
	e.PUT("/api/content", UpdateResource)
	e.DELETE("/api/content", DeleteResource)

	e.Logger.Fatal(e.Start(port))
}