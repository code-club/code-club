class AddWinnerToVote < ActiveRecord::Migration
  def change
	add_column :votes, :winner, :boolean
  end
end
