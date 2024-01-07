package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Group;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import sample.Planets.*;

import java.io.FileInputStream;
import java.io.InputStream;

public class Main extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("sample.fxml"));
        primaryStage.setTitle("Solar System");
        primaryStage.setScene(new Scene(root, 300, 275));

        //Creates the grid
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setVgap(20);
        grid.setHgap(20);
        grid.setPadding(new Insets(25,25,25,25));

        //creates the buttons
        Button btn_Mercury = new Button("Mercury");
        Button btn_Venus = new Button("Venus");
        Button btn_Earth = new Button("Earth");
        Button btn_Mars = new Button("Mars");
        Button btn_Jupiter = new Button("Jupiter");
        Button btn_Saturn = new Button("Saturn");
        Button btn_Uranus = new Button("Uranus");
        Button btn_Neptune = new Button("Neptune");

        //adds the buttons to the grid
        grid.add(btn_Mercury,1,1);
        grid.add(btn_Venus,2,1);
        grid.add(btn_Earth,1,2);
        grid.add(btn_Mars,2,2);
        grid.add(btn_Jupiter,1,3);
        grid.add(btn_Saturn,2,3);
        grid.add(btn_Uranus,1,4);
        grid.add(btn_Neptune,2,4);

        //Calls constructors
        System.out.println(new Mercury(btn_Mercury,primaryStage));
        System.out.println(new Venus(btn_Venus,primaryStage));
        System.out.println(new Earth(btn_Earth,primaryStage));
        System.out.println(new Mars(btn_Mars,primaryStage));
        System.out.println(new Jupiter(btn_Jupiter,primaryStage));
        System.out.println(new Saturn(btn_Saturn,primaryStage));
        System.out.println(new Uranus(btn_Uranus,primaryStage));
        System.out.println(new Neptune(btn_Neptune,primaryStage));

        Scene scene = new Scene(grid,300,275);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
