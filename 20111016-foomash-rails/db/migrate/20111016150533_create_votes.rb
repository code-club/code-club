class CreateVotes < ActiveRecord::Migration
  def change
    create_table :votes do |t|
      t.integer :left_id
      t.integer :right_id

      t.timestamps
    end
  end
end
