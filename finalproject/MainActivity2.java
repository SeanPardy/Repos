package com.example.finalproject;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import java.util.ArrayList;
import java.util.HashMap;

public class MainActivity2 extends AppCompatActivity {
    ListView listView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
//        listView = findViewById(R.id.listView);

        DB_Handler db_handler = new DB_Handler(this);

        ArrayList<HashMap<String,String>> userList = new ArrayList<>();
        userList = db_handler.GetUsers();

//        ListAdapter adapter = new SimpleAdapter(MainActivity2.this,
//                userList,
//                R.layout.row_layout,
//                new String[]{"name","weight","age"},
//                new int[]{R.id.tv_name,R.id.tv_weight,R.id.tv_age});
//        listView.setAdapter(adapter);

    }
}