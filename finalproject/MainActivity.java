package com.example.finalproject;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AbsListView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements MyAdapter.ItemClickListener{

    MyAdapter myAdapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        RecyclerView rv = findViewById(R.id.rv1);
        ArrayList<Integer> myList = new ArrayList<Integer>();
        myList.add(R.drawable.food);
        myList.add(R.drawable.gym);
        myList.add(R.drawable.swimming);

        rv.setLayoutManager(new LinearLayoutManager(this));
        myAdapter = new MyAdapter(this, myList);
        myAdapter.setClickListener(this);
        rv.setAdapter(myAdapter);

    }

    @Override
    public void onItemClick(View view, int position) {
        Toast.makeText(this,"you clicked on "+
                myAdapter.getItem(position)+"on position"+
                position,Toast.LENGTH_SHORT).show();

    }
}