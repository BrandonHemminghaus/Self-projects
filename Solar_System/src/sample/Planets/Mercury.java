package sample.Planets;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

public class Mercury {
    public Mercury(Button btn_mercury, Stage primaryStage) {
        btn_mercury.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                Group root = new Group();
                Scene scene = new Scene(root,500,500);
                primaryStage.setScene(scene);
                primaryStage.show();
            }
        });
    }
}
