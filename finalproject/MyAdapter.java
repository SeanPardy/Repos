package com.example.finalproject;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.ViewHolder> {

    private final ArrayList<Integer> myData;
    private final LayoutInflater myInflater;
    private ItemClickListener myClickListener;

    public MyAdapter(MainActivity context, ArrayList<Integer> myData){
        this.myData = myData;
        this.myInflater =LayoutInflater.from(context);

    }

    void setClickListener(ItemClickListener itemClickListener){
        this.myClickListener = itemClickListener;
    }


    @NonNull
    @Override
    public MyAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = myInflater.inflate(R.layout.activity_main,parent,false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull MyAdapter.ViewHolder holder, int position) {
        String name = String.valueOf(myData.get(position));
        holder.myTextView.setText(name);
    }

    @Override
    public int getItemCount() {
        return myData.size();
    }

    Integer getItem(int id){
        return myData.get(id);
    }

    public interface ItemClickListener{
        void onItemClick(View view, int position);

    }
    public class ViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener {

        TextView myTextView;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            myTextView = itemView.findViewById(R.id.textView);
            itemView.setOnClickListener(this);
        }

        @Override
        public void onClick(View view) {
            if (myClickListener != null) myClickListener.onItemClick(view,getAdapterPosition());

        }

    }

}
